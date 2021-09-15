"""An exercise in remainders and boolean logic."""

__author__ = "730312274"


# Begin your solution here...
given_number: int = int(input("Enter an int: "))
divis_2: int = given_number % 2
divis_7: int = given_number % 7

if divis_2 == 0:
    if divis_7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if divis_7 == 0:
        print("HEELS")
    else:
        print("CAROLINA")