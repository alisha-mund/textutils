import pytest

from textutils.numbers import clamp, percentage


@pytest.mark.parametrize(
    "value, expected",
    [(5, 5), (-1, 0), (11, 10), (0, 0), (10, 10)],
)
def test_clamp(value, expected):
    assert clamp(value, 0, 10) == expected


def test_clamp_invalid_range():
    with pytest.raises(ValueError):
        clamp(5, 10, 0)


@pytest.mark.parametrize(
    "part, total, expected",
    [(1, 4, 25.0), (1, 3, 33.33), (0, 5, 0.0), (5, 5, 100.0)],
)
def test_percentage(part, total, expected):
    assert percentage(part, total) == expected


def test_percentage_zero_total_raises():
    with pytest.raises(ValueError):
        percentage(1, 0)