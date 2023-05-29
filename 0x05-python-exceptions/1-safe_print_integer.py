#!/usr/bin/python3
""" function that prints interger with "{:d}".format() """


def safe_print_interger(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
