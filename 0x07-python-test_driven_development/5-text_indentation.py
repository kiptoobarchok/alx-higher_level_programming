#!/usr/bin/python3
"function definition"


def text_indentation(text):
    "check for str type"
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for char in text:
        print(char, end="")
        if char in ['?', '.', ':']:
            print("\n\n", end="")
