#!/usr/bin/python3
""" function that copies bytecode """


def magic_calculation(a, b):
    new_result = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise ValueError("value of x is too large")
            else:
                new_result += (a ** b) / x
        except ValueError:
            new_result = b + a
            break

    return new_result
