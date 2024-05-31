#!/usr/bin/python3

import sys

print(sys.argv)
print(len(sys.argv))

for i in sys.argv:
    print(f"{sys.argv[i]}")