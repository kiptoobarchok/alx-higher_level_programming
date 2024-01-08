#!/usr/bin/python3
'function that divides 2 integers and returns the result'


def safe_print_division(a, b):
    try:
        res = a / b
        print("Inside result: {}".format(res))
    except ZeroDivisionError:
        res = None
    else:
        print(f"{a} / {b} = {res}")
    finally:
        if res is not None:
            print('{} / {} = {}'.format(a, b, res))