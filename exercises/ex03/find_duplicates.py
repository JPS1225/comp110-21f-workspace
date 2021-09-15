"""Finding duplicate letters in a word."""

__author__ = "730312274"

searched_word: str = input("Enter a word: ")
n: int = 0
x: int = 0
success: int = 0

while n < len(searched_word):
    x = n
    while x > 0:
        if searched_word[n] == searched_word[x - 1]:
            success = success + 1
        else:
            success = success + 0
        x = x - 1
    n = n + 1

if success == 0:
    print("False")
else:
    print("True")