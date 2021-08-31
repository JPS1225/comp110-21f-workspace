"""A program to demonstrate interesting numerical operators in python."""

__author__ = "730312274"

left_number: str = input("Left-hand side: ")
right_number: str = input("Right-hand side: ")
exponent_result: float = (int(left_number) ** int(right_number))
division_result: float = (int(left_number) / int(right_number))
intdivision_result: float = (int(left_number) // int(right_number))
remainder_result: float = (int(left_number) % int(right_number))
print(left_number + " ** " + right_number + " is " + str(exponent_result))
print(left_number + " / " + right_number + " is " + str(division_result))
print(left_number + " // " + right_number + " is " + str(intdivision_result))
print(left_number + " % " + right_number + " is " + str(remainder_result))