"""Read JSONC and replace selected top-level fields without erasing comments."""

import json
import re

TOKENS = re.compile(r'"(?:\\.|[^"\\])*"|//[^\r\n]*|/\*[\s\S]*?\*/|,(?=\s*[}\]])')


def _clean_token(match: re.Match[str]) -> str:
    """Keep strings intact and replace comments/trailing commas with whitespace."""
    token = match.group()
    return token if token.startswith('"') else re.sub(r"[^\r\n]", " ", token)


def document(text: str) -> tuple[dict, str]:
    """Parse settings while retaining source offsets for precise updates."""
    cleaned = TOKENS.sub(_clean_token, text)
    cleaned = TOKENS.sub(_clean_token, cleaned)
    data = json.loads(cleaned) if text else {}
    if not isinstance(data, dict):
        raise ValueError("native project settings must be a JSON object")
    return data, cleaned


def _field_spans(cleaned: str) -> dict[str, tuple[int, int]]:
    """Locate top-level values using JSON decoding rather than matching nested keys."""
    decoder = json.JSONDecoder()
    position = cleaned.index("{") + 1
    spans = {}
    while True:
        position += len(cleaned[position:]) - len(cleaned[position:].lstrip())
        if cleaned[position] == "}":
            return spans
        key, end = decoder.raw_decode(cleaned, position)
        start = cleaned.index(":", end) + 1
        start += len(cleaned[start:]) - len(cleaned[start:].lstrip())
        _, end = decoder.raw_decode(cleaned, start)
        if key in spans:
            raise ValueError(f"duplicate native setting {key}; reconcile first")
        spans[key] = start, end
        position = end
        position += len(cleaned[position:]) - len(cleaned[position:].lstrip())
        if cleaned[position] == ",":
            position += 1


def replace_fields(text: str, fields: dict) -> str:
    """Preserve every byte outside changed native configuration fields."""
    data, cleaned = document(text)
    changes = {key: value for key, value in fields.items() if key not in data or data[key] != value}
    if not changes:
        return text
    if not text:
        return json.dumps(fields, indent=2, ensure_ascii=False) + "\n"
    spans = _field_spans(cleaned)
    edits, missing = [], {}
    for key, value in changes.items():
        if key in spans:
            start, end = spans[key]
            edits.append((start, end, json.dumps(value, indent=2, ensure_ascii=False)))
        else:
            missing[key] = value
    if missing:
        insertion = json.dumps(missing, indent=2, ensure_ascii=False)[1:-1]
        insertion += "," if data else ""
        start = cleaned.index("{") + 1
        edits.append((start, start, insertion))
    for start, end, payload in sorted(edits, reverse=True):
        text = text[:start] + payload + text[end:]
    return text
