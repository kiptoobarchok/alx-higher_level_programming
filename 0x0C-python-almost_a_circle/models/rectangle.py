#!/usr/bin/python3
from .base import Base
"class that inherits from Base"


class Rectangle(Base):
    "defining rectangle attributes"
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        "function to return width of rectangle"
        return self.__width

    @width.setter
    def width(self, value):
        """"
        function to set value of rectangle
        and assert it
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value <= 0:
            raise ValueError("width must be > 0")

        else:
            self.__width = value

    @property
    def height(self):
        "function to get height of rectangle"
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for the rectangle's height
        and assert its value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        "function to get value of X"
        return self.__x

    @x.setter
    def x(self, value):
        "function to set X and assert it's value"
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        else:
            self.__x = value

    @property
    def y(self):
        "function to get Y"
        return self.__y

    @y.setter
    def y(self, value):
        "function to set the value of Y and assert it's value"
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        elif (value < 0):
            raise ValueError("y must be >= 0")

        else:
            self.__y = value

    def area(self):
        "function to return area of rectangle"
        return self.__width * self.__height

    def display(self):
        "fuunction to display the rectangle as # "
        for i in range(self.y):
            print()

        for i in range(self.height):
            print("#" * self.width)

    def update(self, *args, **kwargs):
        "function to update the values of height, width, X and Y"
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        "function to return a customized string"
        return (f"[Rectangle] ({self.id})\
                {self.__x}/{self.__y} - {self.__width}/{self.__height}")
