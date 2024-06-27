#!/usr/bin/python3

'function that checks for lower case'

def isLower(c):
    if (ord(c) in [97, 123]):
        return True
    else:
        return False