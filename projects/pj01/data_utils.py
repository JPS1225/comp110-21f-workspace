"""Utility functions."""

__author__ = "730312274"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of a csv into a table."""
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
    for key in full_table:
        holding_list: list[str] = []
        i = 0
        while i < result_size:
            holding_list.append(full_table[key][i])
            i += 1
        result[key] = holding_list
    return result


def select(full_table: dict[str, list[str]], specific_columns: list[str]) -> dict[str, list[str]]:
    """Makes a new table of rows from a column-oriented table based on a list of row names."""
    result: dict[str, list[str]] = {}
    key_list: list[str] = []
    i = 0
    for key in full_table:
        key_list.append(key)
    while i < len(key_list):
        if key_list[i] in specific_columns:
            result[key_list[i]] = full_table[key_list[i]]
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
            result[f"{key_list2[n]}"] = l1[f"{key_list2[n]}"] + l2[f"{key_list2[n]}"]
        else:
            result[f"{key_list2[n]}"] = l2[f"{key_list2[n]}"]
        n += 1
    return result


def count(haystack: list[str]) -> dict[str, int]:
    """Counts the number of times an item appears in a list."""
    output: dict[str, int] = {}
    i: int = 0
    while i < len(haystack):
        if f"{haystack[i]}" in output:
            output[f"{haystack[i]}"] += 1
        else:
            output[f"{haystack[i]}"] = 1
        i += 1
    return output


def maskmake(full_table: dict[str, list[str]], colname: str, check_value: str) -> list[bool]:
    """Creates masks of column-oriented data given the data, the name of the column to generate the mask from, and a string to check equivalency to."""
    result: list[bool] = []
    col: list[str] = full_table[colname]
    for item in col:
        if item == check_value:
            result.append(True)
        else:
            result.append(False)
    return result


def boollisthead(boollist: list[bool], result_size: int) -> list[bool]:
    """Shows a specified number of rows from a  list of boolean values."""
    result: list[bool] = []
    i: int = 0
    while i < result_size:
        result.append(boollist[i])
        i += 1
    return result


def maskuser(full_table: dict[str, list[str]], mask: list[bool], targetkey: str) -> list[str]:
    """Uses a mask list of Boolean values to mask the values of a specified key in a column-oriented dataset."""
    result: list[str] = []
    for i in range(len(mask)):
        if mask[i]:
            result.append(full_table[targetkey][i])
    return result


def strlisthead(strlist: list[str], result_size: int) -> list[str]:
    """Shows a specified number of rows from a list of integer values."""
    result: list[str] = []
    i: int = 0
    while i < result_size:
        result.append(strlist[i])
        i += 1
    return result


def intconverter(strlist: list[str]) -> list[int]:
    """Converts a list of strings into a list of integers."""
    result: list[int] = []
    for item in strlist:
        result.append(int(item))
    return result


def intlisthead(intlist: list[int], result_size: int) -> list[int]:
    """Shows a specified number of rows from a list of integer values."""
    result: list[int] = []
    i: int = 0
    while i < result_size:
        result.append(intlist[i])
        i += 1
    return result


def averagemachine(intlist: list[int]) -> float:
    """Averages the values in a list of integers."""
    totalsum: int = 0
    i: int = 0
    average: float = 0.0
    while i < len(intlist):
        totalsum += intlist[i]
        i += 1
    average = totalsum / len(intlist)
    return average


def intcount(haystack: list[int]) -> dict[int, int]:
    """Counts the number of times an item appears in a list of integers."""
    output: dict[int, int] = {}
    i: int = 0
    while i < len(haystack):
        if haystack[i] in output:
            output[haystack[i]] += 1
        else:
            output[haystack[i]] = 1
        i += 1
    return output