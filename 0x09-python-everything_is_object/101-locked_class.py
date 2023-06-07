#!/usr/bin/python3
"""program that prevents user from creating new instance attributes"""


class LockedClass:
    """new class"""
    __slots__ = ["first_name"]
