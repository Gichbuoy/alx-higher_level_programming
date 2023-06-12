#!/usr/bin/python3
"""function that inherits from list"""


class MyList(list):
    """class defined is a subclass of builtin class"""
    def print_sorted(self):
        """ defines a function that prints a sorted list in ascending order"""
        print(sorted(self))
