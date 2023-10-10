#!/usr/bin/python3
"function to write to file"


def write_file(filename="", text=""):
    'write string to file'
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
