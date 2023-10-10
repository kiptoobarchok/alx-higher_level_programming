#!/usr/bin/python3
"function to append a filetext"


def append_write(filename="", text=""):
    "appends string to the end of file"
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
