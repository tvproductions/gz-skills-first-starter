"""Verify built artifacts and installed CLI behavior outside the checkout."""

import hashlib
import json
import os
import secrets
import subprocess
import sys
import tarfile
import tempfile
import tomllib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(
    *command: str, cwd: Path, env: dict[str, str] | None = None
) -> subprocess.CompletedProcess[str]:
    """Run a verification command and retain decoded failure diagnostics."""
    return subprocess.run(
        command,
        cwd=cwd,
        env=env,
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
            "examples/application_foundations/pyproject.toml",
            "examples/application_foundations/README.md",
            "examples/application_foundations/settings.example.json",
            "examples/application_foundations/src/example_foundations/configuration.py",
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


def verify_fixture(sdist: Path) -> None:
    """Build the reference from delivered source and verify clean installed use."""
    with tempfile.TemporaryDirectory(prefix="starter-foundations-") as temporary:
        directory = Path(temporary)
        source = directory / "source"
        source.mkdir()
        with tarfile.open(sdist) as archive:
            top = archive.getnames()[0].split("/")[0]
            archive.extractall(source, filter="data")
        fixture = source / top / "examples/application_foundations"
        artifacts = directory / "artifacts"
        sentinel = secrets.token_hex(24)
        protected = directory / "protected-parent-output.txt"
        protected.write_text("parent environment must not change this", encoding="utf-8")
        parent_environment = dict(os.environ) | {
            "EXAMPLE_FOUNDATIONS_CONFIG": str(directory / "missing-parent-config.json"),
            "EXAMPLE_FOUNDATIONS_MESSAGE": "parent override must not load",
            "EXAMPLE_FOUNDATIONS_OUTPUT_FILE": str(protected),
        }
        clean = {
            key: value
            for key, value in parent_environment.items()
            if key not in ("PYTHONPATH", "PYTHONHOME")
            and not key.startswith("EXAMPLE_FOUNDATIONS_")
        }
        clean["EXAMPLE_FOUNDATIONS_TOKEN"] = sentinel
        run(
            "uv",
            "build",
            "--no-sources",
            "--project",
            str(fixture),
            "--out-dir",
            str(artifacts),
            cwd=directory,
            env=clean,
        )
        wheel = artifacts / "example_foundations-0.1.0-py3-none-any.whl"
        with zipfile.ZipFile(wheel) as archive:
            if "example_foundations/py.typed" not in archive.namelist():
                raise ValueError("Reference library is missing its typing marker")
            if any(sentinel.encode() in archive.read(name) for name in archive.namelist()):
                raise ValueError("Fixture distribution leaked a test credential")
        environment = directory / "env"
        run("uv", "venv", "--python", sys.executable, str(environment), cwd=directory, env=clean)
        scripts = environment / ("Scripts" if os.name == "nt" else "bin")
        python = scripts / ("python.exe" if os.name == "nt" else "python")
        command = scripts / (
            "example-foundations.exe" if os.name == "nt" else "example-foundations"
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
            env=clean,
        )
        outside = directory / "outside"
        outside.mkdir()
        config_root = directory / "operator"
        config_root.mkdir()
        settings = config_root / "settings.json"
        settings.write_text(
            '{"schema_version":1,"message":"external settings survive"}', encoding="utf-8"
        )
        before = settings.read_bytes()
        arguments = (
            str(python),
            "-I",
            "-m",
            "example_foundations",
            "--config-root",
            str(config_root),
        )
        result = run(*arguments, cwd=outside, env=clean)
        if protected.read_text(encoding="utf-8") != "parent environment must not change this":
            raise ValueError("Installed fixture followed an inherited output override")
        if json.loads(result.stdout) != {"text": "external settings survive"}:
            raise ValueError("Installed reference did not load external settings")
        if run(str(command), "--version", cwd=outside, env=clean).stdout.strip() != "0.1.0":
            raise ValueError("Installed fixture entry point has the wrong version")
        run(
            str(python),
            "-I",
            "-c",
            "from example_foundations import load_settings, Settings, Overrides",
            cwd=outside,
            env=clean,
        )
        consumer = outside / "consumer.py"
        consumer.write_text(
            'from example_foundations import Settings\ncount: int = Settings("hello", 1, (), None).repeat\n',
            encoding="utf-8",
        )
        run(
            "uv",
            "run",
            "--locked",
            "ty",
            "check",
            "--python",
            str(python),
            str(consumer),
            cwd=ROOT,
            env=clean,
        )
        consumer.write_text(
            'from example_foundations import Settings\ncount: str = Settings("hello", 1, (), None).repeat\n',
            encoding="utf-8",
        )
        rejected = subprocess.run(
            ["uv", "run", "--locked", "ty", "check", "--python", str(python), str(consumer)],
            cwd=ROOT,
            env=clean,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        if (
            rejected.returncode != 1
            or "invalid-assignment" not in rejected.stdout + rejected.stderr
        ):
            raise ValueError("Installed reference types did not reject an invalid consumer")
        run(
            "uv",
            "pip",
            "install",
            "--offline",
            "--no-deps",
            "--reinstall",
            "--python",
            str(python),
            str(wheel),
            cwd=outside,
            env=clean,
        )
        if settings.read_bytes() != before:
            raise ValueError("Code replacement changed operator settings")
        run(*arguments, cwd=outside, env=clean)
        missing = subprocess.run(
            [*arguments, "--config", str(config_root / "missing.json")],
            cwd=outside,
            env=clean,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        if missing.returncode != 2 or missing.stdout:
            raise ValueError("Invalid explicit settings did not fail before output")
        settings.write_text(
            '{"schema_version":1,"credential_ref":"env:EXAMPLE_FOUNDATIONS_TOKEN"}',
            encoding="utf-8",
        )
        clean["EXAMPLE_FOUNDATIONS_TOKEN"] = sentinel
        diagnostics = run(*arguments, "--check-config", cwd=outside, env=clean)
        if clean["EXAMPLE_FOUNDATIONS_TOKEN"] in diagnostics.stdout + diagnostics.stderr:
            raise ValueError("Installed reference leaked an injected credential")


def main() -> None:
    """Inspect archives and exercise the installed helper outside the checkout."""
    metadata = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    version = metadata["project"]["version"]
    distribution = metadata["project"]["name"].replace("-", "_")
    wheel = ROOT / "dist" / f"{distribution}-{version}-py3-none-any.whl"
    sdist = ROOT / "dist" / f"{distribution}-{version}.tar.gz"
    verify_archives(wheel, sdist)
    verify_fixture(sdist)
    with tempfile.TemporaryDirectory(prefix="starter-wheel-") as temporary:
        directory = Path(temporary)
        environment = directory / "env"
        run("uv", "venv", "--python", sys.executable, str(environment), cwd=directory)
        scripts = environment / ("Scripts" if os.name == "nt" else "bin")
        python = scripts / ("python.exe" if os.name == "nt" else "python")
        command = scripts / ("gz-starter.exe" if os.name == "nt" else "gz-starter")
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
        legacy = scripts / (
            "skills-first-starter.exe" if os.name == "nt" else "skills-first-starter"
        )
        if (
            run(str(legacy), "version", cwd=directory).stdout
            != run(str(command), "version", cwd=directory).stdout
        ):
            raise ValueError("Legacy command alias differs from the canonical command")
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
