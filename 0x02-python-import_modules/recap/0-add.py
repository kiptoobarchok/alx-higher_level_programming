#!/usr/bin/python3

# mod = __import__("add_0")

from add_0 import add # type: ignore
a = 1
b = 2
# c = mod.add(a, b)
c = add(a, b)


print(add.__doc__)
print(f"{a} + {b} = {c}")