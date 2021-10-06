"""List utility functions part 2."""

__author__ = "730312274"

# Define your functions below


def only_evens(haystack: list[int]) -> list[int]:
    """Determines the even numbers in a list of integers."""
    output: list[int] = []
    i: int = 0
    while i < len(haystack):
        if haystack[i] % 2 == 0:
            output.append(haystack[i])
        i += 1
    return output


def sub(haystack: list[int], l1: int, l2: int) -> list[int]:
    """Given a list, and integer starting point, and an integer end point, generates a sublist from the start point to the end point."""
    output: list[int] = []
    i: int = 0
    if l1 < 0:
        l1 = 0
    if l2 > len(haystack):
        l2 = len(haystack)
    while i < len(haystack):
        if i >= l1 and i < l2:
            output.append(haystack[i])
        i += 1
    return output


def concat(xs1: list[int], xs2: list[int]) -> list[int]:
    """Makes a ne list of integers that has the contents of two given lists of integers."""
    output: list[int] = []
    output = xs1 + xs2
    return output