"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730312274"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
your_fortune_value = int(randint(1, 10))

print("Your fortune cookie says...")
if your_fortune_value == 1:
    print("You will find success in completing a difficult task.")
else:
    if your_fortune_value == 2:
        print("A new career opportunity will present a fulfilling life.")
    else:
        if your_fortune_value == 3:
            print("You will come into faovr with the one you value most.")
        else:
            if your_fortune_value == 4:
                print("The time is coming for you to show the world your skills.")
            else:
                if your_fortune_value == 5:
                    print("You will recieve great fortune after a hard trial.")
                else:
                    if your_fortune_value == 6:
                        print("A change in personal tastes will open your mind to great possibilities.")
                    else:
                        if your_fortune_value == 7:
                            print("A long journey will bring you great happiness.")
                        else:
                            if your_fortune_value == 8:
                                print("Finding meaning in the friends you have will help you to meet new people.")
                            else:
                                if your_fortune_value == 9:
                                    print("You will soon recieve great prestige for your work in life.")
                                else:
                                    if your_fortune_value == 10:
                                        print("You are about to reach the end of a lengthy journey.")
print("Now, go spread positive vibes!")