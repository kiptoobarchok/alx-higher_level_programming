#!/usr/bin/python3
"function definition"


def print_square(size):
    "function that prints square with character #"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print('#', end=" ")
        print()
