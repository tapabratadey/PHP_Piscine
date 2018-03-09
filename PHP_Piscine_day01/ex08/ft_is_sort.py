#!/usr/bin/python
import sys
def ft_is_sort(arr):
    sorted = False
    temp = 0

    if (len(arr) < 0):
        print "Array is empty"
    for i in range(0, len(arr) - 1):
        if (arr[i] > arr[i+1]):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            return False
    return True
    