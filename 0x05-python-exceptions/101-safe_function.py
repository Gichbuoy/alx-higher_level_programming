#!/usr/bin/python3
""" function that executes a function safely """
import sys


def safe_function(fct, *args):
    try:
        new_result = fct(*args)
        return new_result
    except Exception as e:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
