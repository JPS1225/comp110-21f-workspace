"""Example of writing a function to process a list."""

__author__ = "730312274"


def main() -> None:
    """Entrypoint of program."""
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kevin", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in haystack."""
    # move through each item until needle is found
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1
    return False


if __name__ == "__main__":
    main()