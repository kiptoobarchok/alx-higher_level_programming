#!/usr/bin/python3

mod = __import__("calculator_1")

# from calculator_1 import *

a = 10
b = 5

print(f"{a} + {b} = {mod.add(a,b)}", mod.add.__doc__)
print(f"{a} - {b} = {mod.sub(a,b)}", mod.sub.__doc__)
print(f"{a} * {b} = {mod.mul(a,b)}", mod.mul.__doc__)
print(f"{a} / {b} = {mod.div(a,b)}", mod.div.__doc__)
