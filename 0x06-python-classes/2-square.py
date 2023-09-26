#!/usr/bin/python3

"""Define a class - Square"""


class Square:
    """class to represent the square"""

    def __init__(self, size=0):
        """initialize square
        Args:
           size: Size of new class (int).
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
