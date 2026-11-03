import pytest

from textutils.strings import reverse_words, slugify, truncate


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello World", "hello-world"),
        ("  Python 3.11 rocks!  ", "python-3-11-rocks"),
        ("already-a-slug", "already-a-slug"),
    ],
)
def test_slugify(text, expected):
    assert slugify(text) == expected


def test_truncate_short_text_unchanged():
    assert truncate("hello", 10) == "hello"


def test_truncate_exact_length_unchanged():
    assert truncate("hello", 5) == "hello"


def test_truncate_result_fits_max_len():
    result = truncate("hello world", 8)
    assert result == "hello..."
    assert len(result) <= 8


def test_truncate_custom_suffix():
    assert truncate("hello world", 7, suffix="~") == "hello ~"


def test_reverse_words():
    assert reverse_words("one two  three") == "three two one"