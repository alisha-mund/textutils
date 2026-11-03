import pytest

from textutils.text_stats import char_frequency, word_count


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", 2),
        ("hello   world", 2),
        ("hello\nworld", 2),
        ("one", 1),
        ("", 0),
        ("   ", 0),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected


def test_char_frequency():
    assert char_frequency("Aa b") == {"a": 2, "b": 1}