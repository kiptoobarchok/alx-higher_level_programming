#!/usr/bin/python3
"function to read from file"


def read_file(filename=""):
    "output contents of file"
    with open(filename, 'r' encoding="utf-8") as f:
        print(f.read(), end="")
