"""Practice with dictionaries."""

__author__ = "730312274"

# Define your functions below


def invert(package: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary of strings."""
    output: dict[str, str] = {}
    for key in package:
        if f"{package[key]}" in output:
            raise KeyError("Resultant dictionary will have duplicate keys!")
        else:
            output[f"{package[key]}"] = key
    return output


def favorite_color(package: dict[str, str]) -> str:
    """Determines the most common value in a dictionary of strings."""
    output: str = ""
    count_table: dict[str, int] = {}
    current_high: int = -1
    for key in package:
        if f"{package[key]}" in count_table:
            count_table[f"{package[key]}"] += 1
        else:
            count_table[f"{package[key]}"] = 1
    for key in count_table:
        if count_table[key] > current_high:
            output = key
            current_high = count_table[key]
    return output


def count(haystack: list[str]) -> dict[str, int]:
    """Counts the number of times an item appears in a list."""
    output: dict[str, int] = {}
    i = 0
    while i < len(haystack):
        if f"{haystack[i]}" in output:
            output[f"{haystack[i]}"] += 1
        else:
            output[f"{haystack[i]}"] = 1
        i += 1
    return output