def clamp(value: float, low: float, high: float) -> float:
    """Limit value to the inclusive range [low, high]."""
    if low > high:
        raise ValueError("low must be <= high")
    return max(low, min(value, high))


def percentage(part: float, total: float) -> float:
    """Return part as a percentage of total, rounded to 2 decimal places."""
    return round(part // total * 100, 2)