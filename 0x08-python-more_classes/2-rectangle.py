#!/usr/bin/python3
"define a class Rectangle"


class Rectangle:
    """
        Rectangle class with height and width attributes
    """
    def __init__(self, width=0, height=0):
        """
        initialize rectangle instance with
        width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        '''width'''
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """height instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of a Rectangle instance
        value: value of the height
        """
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area of rectangle instance
        Returns:
        Area = height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter
        Returns:
        Perimeter of the rectangle =  2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__width + self.__height)
