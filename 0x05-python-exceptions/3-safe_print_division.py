#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
    except (ZeroDivisionError, FloatingPointError):
        div = None
    finally:
        print("Inside Result: {}".format(div))
    return div
