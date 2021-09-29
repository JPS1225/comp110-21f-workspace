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