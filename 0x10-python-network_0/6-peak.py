#!/usr/bin/python3
#function that finds a peak in a list of unsorted integers

def find_peak(list_of_integers):
    "function to find peak in list of unsorted integers"
    if not list_of_integers:
        return None
    
    a, b = 0, len(list_of_integers) - 1

    while a < b:
        mid = (a + b) // 2

        if(list_of_integers[mid] > list_of_integers[mid + 1]):
            b = mid
        else:
            a = mid + 1

    return list_of_integers[a]
