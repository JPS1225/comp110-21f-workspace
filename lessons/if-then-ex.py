"""Practice with if-then-else statements."""

__author__ = "730312274"

choice: int = int(input("Enter a number: "))

if choice < 75 or choice == 75:
    if choice < 50:
        if choice < 25:
            print("A")
        else:
            print("B")
    else: 
        print("D")
else:
    print("C")