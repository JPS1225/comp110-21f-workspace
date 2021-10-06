"""Example of writing a test subject."""

__author__ = "730312274"

def sum(xs: list[float]) -> float:
    total: float = 0.0
    i: int = 0
    while i < len(xs):
        total += xs[i]
        i += 1
    return total
