#!/usr/bin/python3
"""square that defines a square """


class Square:
    """ create a class square """

    def __init__(self, size=0):
        """initialize variables"""
        self.size = size

    @property
    def size(self):
        """ define method square that takes no arguments"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ define method that takes argument value"""
        if not isinstance(value, int):
            raise TypeError("size must be an interger")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ define method area"""
        return (self.__size * self.__size)
