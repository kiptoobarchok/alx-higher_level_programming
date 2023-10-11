#!/usr/bin/python3
"define a class that inherits from int"


class MyInt(int):
    "inverted operators"
    def __eq__(self, value):
        return self.real != (value)

    def __ne__(self, value):
        return self.real == (value)
