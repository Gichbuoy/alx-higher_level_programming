#!/usr/bin/python3
""" class that defines a square """


class Square:
    """ create a class Square """

    def __init__(self, size):
        """initialize variable size"""
        self.size = size

    @property
    def size(self):
        """ define current size of square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise valueError("size must be >= 0")
        self.__size = value

    def area(self):
        """define method area"""
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
