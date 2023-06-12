#!/usr/bin/python3
""" function that returns a list of available attributes and methods"""


def lookup(obj):
    """define function that takes 1 parameter"""
    return dir(obj)
