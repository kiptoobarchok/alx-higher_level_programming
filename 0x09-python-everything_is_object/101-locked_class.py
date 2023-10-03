#!/usr/bin/python3
"Define a class"


class Lockedclass:
    "prevent user from instantiating new lockedClass"
    __slots__= ['first_name']
