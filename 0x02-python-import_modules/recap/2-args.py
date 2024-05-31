#!/usr/bin/python3

import sys

if (len(sys.argv) > 1):
    for i in range(0, len(sys.argv)):
        print(f" {i} : {sys.argv[i]}")
else:
    print("no command line arguements")