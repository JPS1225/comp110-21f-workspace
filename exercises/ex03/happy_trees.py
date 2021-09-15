"""Drawing forests in a loop."""

__author__ = "730312274"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
n: int = 0
forest: str = ""

while n <= (depth - 1):
    forest = forest + TREE
    print(forest)
    n = n + 1
