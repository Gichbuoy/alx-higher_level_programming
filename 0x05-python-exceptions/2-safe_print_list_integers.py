#!/usr/bin/python3
""" function that prints the first x elements of a list and only intergers"""


def safe_print_list_integers(my_list=[], x=0):
    random = 0
    for a in range(0, x):
        try:
            print("{:d}".format(my_list[a]), end="")
            random += 1
        except (ValueError, TypeError):
            continue

    print("")
    return (random)
