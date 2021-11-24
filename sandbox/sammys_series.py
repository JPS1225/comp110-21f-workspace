"""A mathematical series."""

__author__ = "730312274"

from matplotlib import pyplot as plt

endpoint: int = int(input("Where would you like to stop? "))
i: int = 1
last_result: float = 0.3
points: dict[int, float] = {}

while i <= endpoint:
    points[i] = last_result
    last_result = last_result + ((1 - last_result) * 0.5)
    i += 1

myList = points.items()
myList = sorted(myList) 
x, y = zip(*myList) 

plt.plot(x, y)
plt.show()