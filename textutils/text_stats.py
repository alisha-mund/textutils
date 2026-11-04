from collections import Counter


def word_count(text: str) -> int:
    """Count whitespace-separated words in text."""
    # Return 0 for empty or whitespace-only strings
    if not text or not text.strip():
        return 0
    # Use default split() to split on any whitespace and collapse consecutive whitespace
    return len(text.split())


def char_frequency(text: str) -> dict[str, int]:
    """Count each non-whitespace character, case-insensitive."""
    return dict(Counter(c for c in text.lower() if not c.isspace()))
