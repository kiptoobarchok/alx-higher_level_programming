#!/usr/bin/python3

import random
number = random.randint(-100, 100)

if (number > 0):
    print(f"{number} is +ve")
elif (number == 0):
    print(f"{number} is 0")
else:
    print(f"{number} is -ve")

