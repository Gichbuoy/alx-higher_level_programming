#!/usr/bin/python3
"""function that prints the last digit of a number """


def print_last_digit(number):
    if number < 0:
        last_digit = number % -(10)
        print(-(last_digit), end="")
    elif:
        last_digit = number % 10
        print(last_digit, end="")
    return abs(last_digit)
