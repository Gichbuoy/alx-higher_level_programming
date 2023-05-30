#!/usr/bin/python3
"""square that defines a square """


class Square:
    """ create a square called class"""

    def __int__(self, size=0):
        """initializes variables """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """define variable area"""
        return (self.__size * self.__size)
