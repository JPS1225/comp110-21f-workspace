"""Utility functions."""

__author__ = "730312274"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of a scv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a row-oriented table into a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(full_table: dict[str, list[str]], result_size: int) -> dict[str, list[str]]:
    """Shows a specified number of rows from a column-based table."""
    result: dict[str, list[str]] = {}
    key_list: list[str] = []
    for key in full_table:
        key_list.append(key)
    first_row: list[str] = full_table[key_list[0]]
    for column in first_row:
        i: int = 0
        holding_list: list[str] = []
        while i < result_size:
            item: str = column[i]
            holding_list.append(item)
            i += 1
        result[column] = holding_list
    return result


def select(full_table: dict[str, list[str]], specific_columns: list[str]) -> dict[str, list[str]]:
    """Makes a new table of rows from a column-oriented table based on a list of row names."""
    result: dict[str, list[str]] = {}
    key_list: list[str] = []
    for key in full_table:
        key_list.append(key)
    for item in specific_columns:
        i: int = 0
        while i < len(key_list):
            if item == key_list[i]:
                result[f"{key_list[i]}"] = full_table[key_list[i]]
            i += 1
    return result


def concat(l1: dict[str, list[str]], l2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column-oriented tables into a single column-oriented table."""
    result: dict[str, list[str]] = {}
    key_list1: list[str] = []
    key_list2: list[str] = []
    for key in l1:
        key_list1.append(key)
    for key in l2:
        key_list2.append(key)
    i: int = 0
    while i < len(l1):
        result[f"{key_list1[i]}"] = l1[f"{key_list1[i]}"]
        i += 1
    n: int = 0
    while n < len(l2):
        if f"{key_list2[n]}" in result:
            result[f"{key_list2[n]}"] = l1[f"{key_list1[n]}"] + l2[f"{key_list1[n]}"]
        else:
            result[f"{key_list2[n]}"] = l2[f"{key_list1[n]}"]
        n += 1
    return result


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