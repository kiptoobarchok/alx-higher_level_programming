#!/usr/bin/env python3

'function to write last digit of a number'

def print_last_digit(number):
    if (number < 0):
        number *= -1

    last = number % 10

    return last