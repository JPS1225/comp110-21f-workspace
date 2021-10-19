"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730312274"


import pytest
from exercises.ex06.dictionaries import invert, favorite_color, count


# Testing invert
def test_invert_empty() -> None:
    """Tests invert works on empty lest."""
    xs: dict = {}
    assert invert(xs) == {}


def test_invert_letters() -> None:
    """Tests invert works on a dictionary of letters."""
    xs: dict = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_long_strings() -> None:
    """Tests invert works on longer strings like words."""
    xs: dict = {'apple': 'cat', 'crab': 'pizza'}
    assert invert(xs) == {'cat': 'apple', 'pizza': 'crab'}


def test_invert_result_error() -> None:
    """Tests invery returns an error when resultant dict will have duplicate keys."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


# Testing favorite_color
def test_favorite_empty() -> None:
    """Tests favorite_color works on empty lest."""
    xs: dict = {}
    assert favorite_color(xs) == ""


def test_favorite_clear_winner() -> None:
    """Test favorite_color when there is a clear favorite color."""
    xs: dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_tie_all() -> None:
    """Test favorite_color returns first color mentioned when there there is a tie among two or more colors."""
    xs: dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "green"}
    assert favorite_color(xs) == "yellow"


def test_favorite_tie_some() -> None:
    """Test favorite_color returns first color mentioned when there there is a tie among two or more colors that have two or more hits."""
    xs: dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "green", "Jackson": "blue", "Larry": "green"}
    assert favorite_color(xs) == "blue"


# Testing count
def test_count_empty() -> None:
    """Tests count works on empty lest."""
    xs: list = []
    assert count(xs) == {}


def test_count_unique_items() -> None:
    """Tests count can count a list of unique items."""
    xs: list = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
    assert count(xs) == {"Red": 1, "Orange": 1, "Yellow": 1, "Green": 1, "Blue": 1, "Purple": 1}


def test_count_some_dupes() -> None:
    """Tests count can count up duplicate itmes."""
    xs: list = ["One", "Two", "Two", "Three"]
    assert count(xs) == {"One": 1, "Two": 2, "Three": 1}


def test_count_all_same() -> None:
    """Tests count can tally a whole list of duplicate phrases."""
    xs: list = ["Squirrel!", "Squirrel!", "Squirrel!", "Squirrel!", "Squirrel!"]
    assert count(xs) == {"Squirrel!": 5}