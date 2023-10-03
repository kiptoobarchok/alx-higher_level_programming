#!/usr/bin/python3
"class to define a Rectangle"


class Rectangle:
    "Rectangle class with width and height attrubutes"

    def __init__(self, width=0, height=0):
        """Initialize rectangle instance
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get  Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of Rectangle instance
        value: value of the width, must be a (pos) int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        "get the height of a Rectangle instance"
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
			value: value of the height, must be a (pos) integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of a Rectangle instance
			Return:
            Area of rectangle = height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance
           Return:
            Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
