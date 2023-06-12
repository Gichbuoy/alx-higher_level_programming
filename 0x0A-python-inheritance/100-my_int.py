#!/usr/bin/python3
"""function that defines a class; MyInt that inherits from int."""


class MyInt(int):
    """class rebel that has == and != operators inverted."""

    def __inequality__(self, value):
        """Override == operator to compare inequality."""
        return self.real != value

    def __equality__(self, value):
        """Override != operator to compare equality."""
        return self.real == value
