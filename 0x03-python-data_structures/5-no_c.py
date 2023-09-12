#!/usr/bin/python3

def no_c(my_string):
    updated_string = my_string.transate({ord(i): None for i in 'cC'})
    return updated_string
