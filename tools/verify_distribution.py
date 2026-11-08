"""Verify built artifacts and installed CLI behavior outside the checkout."""

import hashlib
import json
import os
import subprocess
import sys
import tarfile
import tempfile
import tomllib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*command: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    """Run a verification command and retain decoded failure diagnostics."""
    return subprocess.run(
        command,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        errors="strict",
        capture_output=True,
        check=True,
    )


def verify_archives(wheel: Path, sdist: Path) -> None:
    """Allow only the owned update skill and verify every packaged resource."""
    with zipfile.ZipFile(wheel) as archive:
        names = archive.namelist()
        skill = "templates/skills/update-gz-template/SKILL.md"
        allowed = f"skills_first_starter/resources/{skill}"
        if {name for name in names if name.endswith("/SKILL.md")} != {allowed}:
            raise ValueError("Wheel must contain exactly the template-owned update skill")
        if any(name.startswith(("tests/", "tools/")) for name in names):
            raise ValueError("Unexpected development files or skills in wheel")
        if (
            "skills_first_starter/resources/docs/engineering/architectural-decisions.md"
            not in names
        ):
            raise ValueError("Wheel is missing the canonical ADR policy")
        for relative in (
            "bundle.json",
            ".agents/plugins/marketplace.json",
            ".claude-plugin/marketplace.json",
            "templates/AGENTS.skills-first.md",
            skill,
            "docs/engineering/architectural-decisions.md",
        ):
            content = archive.read(f"skills_first_starter/resources/{relative}")
            if content != (ROOT / relative).read_bytes():
                raise ValueError(f"Wheel resource differs from authority: {relative}")
    with tarfile.open(sdist) as archive:
        names = archive.getnames()
        if not any(name.endswith("/tests/test_starter.py") for name in names):
            raise ValueError("Source distribution is missing adoption tests")
        for relative in (
            ".github/dependabot.yml",
            "baselines/xplane/pyproject.toml",
            "baselines/xplane/uv.lock",
            "baselines/xplane/.python-version",
            "baselines/xplane/README.md",
            "tools/engineering/cognitive_qualification.py",
            "tools/engineering/cognitive_check.py",
            "tools/engineering/fixtures/cognitive-v1.json",
        ):
            if not any(name.endswith(f"/{relative}") for name in names):
                raise ValueError(f"Source distribution is missing baseline input: {relative}")
        if any("/.venv/" in name for name in names):
            raise ValueError("Source distribution contains a development environment")


def verify_native_hosts(command: Path, directory: Path) -> None:
    """Exercise new host configuration and repair from the installed artifact."""
    for host, config, surface in (
        ("claude", ".claude/settings.json", ".claude"),
        ("opencode", "opencode.json", ".agents"),
    ):
        target = directory / host
        target.mkdir()
        args = (
            str(command),
            "configure",
            "--project",
            str(target),
            "--host",
            host,
            "--starter-ref",
            "a" * 40,
        )
        run(*args, "--apply", cwd=directory)
        if not (target / config).is_file():
            raise ValueError(f"Installed helper omitted {host} configuration")
        if (target / surface / "skills/update-gz-template/SKILL.md").read_bytes() != (
            ROOT / "templates/skills/update-gz-template/SKILL.md"
        ).read_bytes():
            raise ValueError(f"Installed helper omitted {host} update skill")
        if json.loads(run(*args, "--apply", cwd=directory).stdout)["writes"]:
            raise ValueError(f"Installed {host} configuration is not idempotent")
        lock = (target / ".skills-first/bundle.lock.json").read_bytes()
        run(
            str(command),
            "localize",
            "--project",
            str(target),
            "--host",
            host,
            "--starter-ref",
            "a" * 40,
            "--apply",
            cwd=directory,
        )
        if (target / ".skills-first/bundle.lock.json").read_bytes() != lock:
            raise ValueError(f"Installed {host} scope repair changed adoption provenance")


def verify_policy_modes(command: Path, directory: Path) -> None:
    """Verify both policy access forms from an installed wheel without a checkout."""
    source = (ROOT / "docs/engineering/architectural-decisions.md").read_bytes()
    for host in ("codex", "claude", "opencode"):
        for mode in ("link", "local"):
            target = directory / f"policy-{host}-{mode}"
            target.mkdir()
            args = (
                str(command),
                "configure",
                "--project",
                str(target),
                "--starter-ref",
                "a" * 40,
                "--host",
                host,
            )
            run(*args, "--adr-policy", mode, cwd=directory)
            if list(target.iterdir()):
                raise ValueError("Installed policy preview wrote files")
            run(*args, "--adr-policy", mode, "--apply", cwd=directory)
            local = target / ".skills-first/architectural-decisions.md"
            if mode == "local" and local.read_bytes() != source:
                raise ValueError("Installed local policy differs from the canonical bytes")
            if mode == "link" and local.exists():
                raise ValueError("Installed link mode created a policy copy")
            lock = json.loads((target / ".skills-first/bundle.lock.json").read_bytes())
            if lock["adr_policy"]["source_sha256"] != hashlib.sha256(source).hexdigest():
                raise ValueError("Installed policy provenance hash differs")
            if json.loads(run(*args, "--apply", cwd=directory).stdout)["writes"]:
                raise ValueError("Installed helper did not preserve policy selection")
            status = json.loads(
                run(str(command), "status", "--project", str(target), cwd=directory).stdout
            )
            if status["adr_policy"]["mode"] != mode or status["runtime_readiness"] != "unverified":
                raise ValueError("Installed policy status changed selection or claimed readiness")


def main() -> None:
    """Inspect archives and exercise the installed helper outside the checkout."""
    metadata = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    version = metadata["project"]["version"]
    wheel = ROOT / "dist" / f"skills_first_starter-{version}-py3-none-any.whl"
    sdist = ROOT / "dist" / f"skills_first_starter-{version}.tar.gz"
    verify_archives(wheel, sdist)
    with tempfile.TemporaryDirectory(prefix="starter-wheel-") as temporary:
        directory = Path(temporary)
        environment = directory / "env"
        run("uv", "venv", "--python", sys.executable, str(environment), cwd=directory)
        scripts = environment / ("Scripts" if os.name == "nt" else "bin")
        python = scripts / ("python.exe" if os.name == "nt" else "python")
        command = scripts / (
            "skills-first-starter.exe" if os.name == "nt" else "skills-first-starter"
        )
        run(
            "uv",
            "pip",
            "install",
            "--offline",
            "--no-deps",
            "--python",
            str(python),
            str(wheel),
            cwd=directory,
        )
        run(str(command), "validate", cwd=directory)
        result = run(str(python), "-I", "-m", "skills_first_starter", "version", cwd=directory)
        if json.loads(result.stdout)["template_version"] != version:
            raise ValueError("Installed version differs from project metadata")
        target = directory / "adopter"
        target.mkdir()
        args = (str(command), "configure", "--project", str(target), "--starter-ref", "a" * 40)
        run(*args, cwd=directory)
        if list(target.iterdir()):
            raise ValueError("Installed preview wrote project files")
        run(*args, "--apply", cwd=directory)
        if (target / ".agents/skills/update-gz-template/SKILL.md").read_bytes() != (
            ROOT / "templates/skills/update-gz-template/SKILL.md"
        ).read_bytes():
            raise ValueError("Installed helper did not seed the canonical update skill")
        repeated = json.loads(run(*args, "--apply", cwd=directory).stdout)
        if repeated["writes"]:
            raise ValueError("Installed repeated adoption was not a no-op")
        status = json.loads(
            run(str(command), "status", "--project", str(target), cwd=directory).stdout
        )
        if status["runtime_readiness"] != "unverified":
            raise ValueError("Installed helper falsely claimed runtime readiness")
        verify_native_hosts(command, directory)
        verify_policy_modes(command, directory)
        refused = subprocess.run(
            [str(command), "configure", "--project", str(target)],
            cwd=directory,
            text=True,
            encoding="utf-8",
            errors="strict",
            capture_output=True,
            check=False,
        )
        if refused.returncode != 2:
            raise ValueError("Installed helper inferred provenance outside a starter checkout")
    print("Wheel resources, sdist contents and isolated installed CLI checks passed.")


if __name__ == "__main__":
    main()
