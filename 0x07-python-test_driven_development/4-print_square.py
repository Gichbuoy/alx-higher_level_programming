#!/usr/bin/python3
"""program that prints square with # symbol"""


def print_square(size):
    """define a function that print size of square"""

    # Check if size is an integer and is not negative
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
