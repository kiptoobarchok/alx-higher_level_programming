#!/usr/bin/python3

"""define class - Square"""


class Square:
    """class to represent Square"""

    def __init__(self, size=0):
        """initialize new class
        Args:
            size: size of new class (int)
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return : current area of square"""
        return (self.__size * self.__size)
