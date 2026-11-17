"""Pure rendering decisions receive values, never hidden process inputs."""


def render_message(message: str, repeat: int, tags: tuple[str, ...]) -> str:
    """Render an ordered tagged message a bounded number of times."""
    prefix = "".join(f"[{tag}]" for tag in tags)
    line = f"{prefix} {message}" if prefix else message
    return "\n".join(line for _ in range(repeat))
