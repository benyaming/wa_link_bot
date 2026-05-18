from __future__ import annotations

import re

_PHONE_CANDIDATE_RE = re.compile(r"(?:\+|00)?\d[\d\s().-]{5,}\d")


def extract_whatsapp_number(
    text: str,
    *,
    default_country_code: str = "972",
) -> str | None:
    """Return a normalized E.164-ish number with a leading plus sign.

    The parser accepts free-form text such as "+972 54-444-5811" or
    "call 0544445811". Local numbers starting with 0 are converted using
    the configured default country code.
    """
    country_code = _digits_only(default_country_code)
    if not country_code:
        raise ValueError("default_country_code must contain at least one digit")

    for raw_candidate in _PHONE_CANDIDATE_RE.findall(text):
        normalized = _normalize_candidate(raw_candidate, country_code)
        if normalized is not None:
            return normalized

    compact = "".join(ch for ch in text.strip() if ch.isdigit() or ch == "+")
    return _normalize_candidate(compact, country_code)


def whatsapp_link(phone_number: str) -> str:
    return f"https://wa.me/{phone_number}"


def _normalize_candidate(candidate: str, country_code: str) -> str | None:
    candidate = candidate.strip()
    if not candidate:
        return None

    has_plus = candidate.startswith("+")
    digits = _digits_only(candidate)

    if len(digits) < 7 or len(digits) > 15:
        return None

    if candidate.startswith("00"):
        digits = digits[2:]
    elif not has_plus and digits.startswith("0"):
        digits = f"{country_code}{digits[1:]}"

    if len(digits) < 7 or len(digits) > 15:
        return None

    return f"+{digits}"


def _digits_only(value: str) -> str:
    return "".join(ch for ch in value if ch.isdigit())
