#!/usr/bin/env python3

'function to change string to uppercase'

def toUppercase(text):
    upper = ""
    for i in text:
        if ord('a') <= ord(i) <=ord('z'):
            new = chr(ord(i) - 32)
        else:
            new = i
        upper += new
    print(upper)