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
    if max_len <= len(suffix):
        return suffix[:max_len]
    available = max_len - len(suffix)
    return text[:available] + suffix


def reverse_words(text: str) -> str:
    """Reverse the order of words, collapsing whitespace to single spaces."""
    return " ".join(reversed(text.split()))
