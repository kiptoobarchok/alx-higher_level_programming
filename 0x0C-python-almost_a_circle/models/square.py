#!/usr/bin/python3
"define class square inheriting from regctangle"
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        'Initialize square that inherits all attributes of rectangle'
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def to_dictionary(self):
        "return dictionary representation of square"
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self) -> str:
        return "[Square] ({}) {}/{} - {}".fromat(self.id, self.x,
                                                 self.y,self.width)
