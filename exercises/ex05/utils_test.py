"""Unit tests for list utility functions."""

__author__ = "730312274"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


# Testing only_evens
def test_evens_empty_list() -> None:
    """Tests only_evens on an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_evens_even_odd_mix() -> None:
    """Test only_evens with a mix of evens and odds."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(xs) == [2, 4]


def test_evens_only_odds() -> None:
    """Tests only_evens with only odd numbers."""
    xs: list[int] = [1, 3, 5, 7]
    assert only_evens(xs) == []


def test_evens_only_evens() -> None:
    """Tests only_evens with only even numbers."""
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


def test_evens_out_order() -> None:
    """Tests only_evens with a mix of odd and even numbers out of order to ensure evens order is maintained."""
    xs: list[int] = [5, 2, 3, 6, 1, 4]
    assert only_evens(xs) == [2, 6, 4]


# Testing sub
def test_sub_typical_length() -> None:
    """Tests sub for a standard list and standard list length."""
    xs: list[int] = [10, 20, 30, 40]
    l1: int = 1
    l2: int = 3
    assert sub(xs, l1, l2) == [20, 30]


def test_sub_order() -> None:
    """Tests sub to ensure list order is maintained in the sublist."""
    xs: list[int] = [20, 40, 10, 30]
    l1: int = 1
    l2: int = 3
    assert sub(xs, l1, l2) == [40, 10]


def test_sub_negative_start() -> None:
    """Tests sub to ensure if start index is negative, sublist starts from beginning of parent list."""
    xs: list[int] = [10, 20, 30, 40]
    l1: int = -3
    l2: int = 3
    assert sub(xs, l1, l2) == [10, 20, 30]


def test_sub_large_end() -> None:
    """Tests sub to ensure if end index is greater than length of parent list, end with end of parent list."""
    xs: list[int] = [10, 20, 30, 40]
    l1: int = 1
    l2: int = 10
    assert sub(xs, l1, l2) == [20, 30, 40]


def test_sub_zero_length() -> None:
    """Tests sub when the list has no length."""
    xs: list[int] = [10, 20, 30, 40]
    l1: int = 1
    l2: int = 1
    assert sub(xs, l1, l2) == []


def test_sub_start_greater_length() -> None:
    """Tests to return an empty list if the start index is greater than the length of the parent list."""
    xs: list[int] = [10, 20, 30, 40]
    l1: int = 100
    l2: int = 120
    assert sub(xs, l1, l2) == []


def test_negative_list_end() -> None:
    """Tests to return an empty list if the end index is less than zero."""
    xs: list[int] = [10, 20, 30, 40]
    l1: int = -5
    l2: int = -3
    assert sub(xs, l1, l2) == []


def test_negative_list_lenth() -> None:
    """Tests to return an empty list if the starting index is greater than the ending index."""
    xs: list[int] = [10, 20, 30, 40]
    l1: int = 3
    l2: int = 1
    assert sub(xs, l1, l2) == []


# Testing concat
def test_concat_standard() -> None:
    """Tests contact can combine two lists standard."""
    xs1: list[int] = [10, 20, 30]
    xs2: list[int] = [40, 50, 60]
    assert concat(xs1, xs2) == [10, 20, 30, 40, 50, 60]


def test_concat_both_empty() -> None:
    """Tests contact produces an empty list when combining two empty lists."""
    xs1: list[int] = []
    xs2: list[int] = []
    assert concat(xs1, xs2) == []


def test_concat_first_empty() -> None:
    """Tests contact when the first list is empty."""
    xs1: list[int] = []
    xs2: list[int] = [40, 50, 60]
    assert concat(xs1, xs2) == [40, 50, 60]


def test_contact_second_empty() -> None:
    """Tests contact when the second list is empty."""
    xs1: list[int] = [10, 20, 30]
    xs2: list[int] = []
    assert concat(xs1, xs2) == [10, 20, 30]


def test_concat_order() -> None:
    """Tests contact to ensure order is maintained when combining."""
    xs1: list[int] = [30, 10, 20]
    xs2: list[int] = [60, 40, 50]
    assert concat(xs1, xs2) == [30, 10, 20, 60, 40, 50]


def test_concat_first_long() -> None:
    """Tests contact to ensure it can combine when first list is longer than second."""
    xs1: list[int] = [10, 20, 30, 40]
    xs2: list[int] = [50, 60, 70]
    assert concat(xs1, xs2) == [10, 20, 30, 40, 50, 60, 70]


def test_concat_second_long() -> None:
    """Tests contact to ensure it can combine when second list is longer than first."""
    xs1: list[int] = [10, 20, 30]
    xs2: list[int] = [40, 50, 60, 70]
    assert concat(xs1, xs2) == [10, 20, 30, 40, 50, 60, 70]


def test_concat_duplicate_items() -> None:
    """Tests contact to ensure duplicate items acorss lists show up separately."""
    xs1: list[int] = [10, 20, 30]
    xs2: list[int] = [20, 30, 40]
    assert concat(xs1, xs2) == [10, 20, 30, 20, 30, 40]