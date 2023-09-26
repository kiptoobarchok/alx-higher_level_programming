#!/usr/bin/python3

"""Define a square"""


class Square:
    """class to represent square"""

    def __init__(self, size=0):
        """Initialize new square.
        Args:
            size : size of new class.
        """
        self.size = size

    @property
    def size(self):
        """return current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area"""
        return (self.__size ** 2)
