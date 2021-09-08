"""Counting letters in a string."""

__author__ = "730312274"


# Begin your solution here...
letter_search: str = input("What letter do you want to search for?: ")
searched_word: str = input("Enter a word: ")
n: int = 0
success: int = 0

while n < len(searched_word):
    if searched_word[n] == letter_search:
        success = success + 1
    else:
        success = success + 0
    n = n + 1
print("Count: " + str(success))