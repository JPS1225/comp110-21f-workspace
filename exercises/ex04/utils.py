"""List utility functions."""

__author__ = "730312274"


# TODO: Implement your functions here.


def all(haystack: list[int], needle: int) -> bool:
    """Determines if a list of integers are all the same integer."""
    i: int = 0

    while i < len(haystack):
        item: int = haystack[i]
        if item != needle:
            return False
        i = i + 1
    return True


def is_equal(l1: list[int], l2: list[int]) -> bool:
    if l1 != l2:
        return False
    return True


def max(haystack: list[int]) -> int:
    if len(haystack) == 0:
        raise ValueError("max() arg is an empty List")
    current_high: int = 0
    i: int = 0
    while i < len(haystack):
        if haystack[i] > current_high:
            current_high = haystack[i]
        i = i + 1
    return(current_high)