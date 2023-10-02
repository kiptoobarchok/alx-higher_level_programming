#!/usr/bin/python3
"simple class definition of a rectangle"


class Rectangle:
    "rectangle class with height and width attributes"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of a Rectangle instance
            value: value of the width (pos int)
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
            value: value of the height (positive)
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
