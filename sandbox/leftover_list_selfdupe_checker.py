def all(haystack: list[int]) -> bool:
    n: int = 0
    x: int = 0
    success: int = 0

    while n < len(haystack):
        x = n
        while x > 0:
            if haystack[n] != haystack[x - 1]:
                success = success + 1
            else:
                success = success + 0
            x = x - 1
            print(success)
        n = n + 1
    if success == 0:
        return True
    else:
        return False


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


def column_limiter(full_table: dict[str, list[str]], result_size: int) -> dict[str, list[str]]:
    """Shows a specified number of columns from a column-oriented table."""
    result: dict[str, list[str]] = {}
    i = 0
    key_list: list[str] = []
    for key in full_table:
        key_list.append(key)
    while i < result_size:
        for key in full_table:
            result[key_list[i]] = full_table[key_list[i]]
        i += 1
    return result