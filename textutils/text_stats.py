from collections import Counter


def word_count(text: str) -> int:
    """Count whitespace-separated words in text."""
    return len(text.split(" "))


def char_frequency(text: str) -> dict[str, int]:
    """Count each non-whitespace character, case-insensitive."""
    return dict(Counter(c for c in text.lower() if not c.isspace()))