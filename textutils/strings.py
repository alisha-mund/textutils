import re


def slugify(text: str) -> str:
    """Lowercase, trim, and replace runs of non-alphanumeric characters with single hyphens."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    """Shorten text so the result, including the suffix, is at most max_len characters."""
    if len(text) <= max_len:
        return text
    return text[:max_len] + suffix


def reverse_words(text: str) -> str:
    """Reverse the order of words, collapsing whitespace to single spaces."""
    return " ".join(reversed(text.split()))