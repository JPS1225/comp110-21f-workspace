"""A program to compare two numbers with relational operators."""

__author__ = "730312274"

left_number: str = input("Left-hand side: ")
right_number: str = input("Right-hand side: ")
lesser_result: str = str(int(left_number) < int(right_number))
greater_or_equal_result: str = str(int(left_number) >= int(right_number))
equal_result: str = str(int(left_number) == int(right_number))
not_equal_result: str = str(int(left_number) != int(right_number))
print(left_number + " < " + right_number + " is " + lesser_result)
print(left_number + " >= " + right_number + " is " + greater_or_equal_result)
print(left_number + " == " + right_number + " is " + equal_result)
print(left_number + " != " + right_number + " is " + not_equal_result)