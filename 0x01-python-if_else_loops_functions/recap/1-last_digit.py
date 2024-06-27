#!/usr/bin/python3

import random
num = random.randint(-10000, 10000)

if (num < 0):
    num_pos = num * -1

last_digit = num_pos % 10


if (last_digit > 5):
    print(f"last digit of {num} is {last_digit} and is greater than 5")
elif (last_digit == 0):
    print(f"last digit of {num} is {last_digit}")
elif (last_digit < 6 )  and (last_digit != 0):
    print(f"last digit of {num} is {last_digit} and is less than 6 and not 0")
