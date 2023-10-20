#!/usr/bin/python3
"Define class rectangle inheriting from Base"
from models.base import Base


class Rectangle(Base):
    "Define a class rectangle inheriting from Base"
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        "getter for width"
        return self.__width

    @width.setter
    def width(self, value):
        "set the value of width"
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        "get the value of height"
        return self.__height

    @height.setter
    def height(self, value):
        "set value of height"
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        "get value of x"
        return self.__x

    @x.setter
    def x(self, value):
        "set the value of x"
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        "get the value of y"
        return self.__y

    @y.setter
    def y(self, value):
        "set the value of y"
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        "calculate area and return its value"
        return self.width * self.height

    def display(self):
        if self.width == 0 or self.width == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def to_dictionary(self):
        "return dictionary representation of rectangle"
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        "return __str__ representation of rectangle"
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
