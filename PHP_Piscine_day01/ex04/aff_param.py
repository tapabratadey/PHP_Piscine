#!/usr/bin/python
import sys
def aff_param():
    arg = len(sys.argv) - 1
    place = 1
    while (place <= arg):
        print sys.argv[place]
        place += 1
aff_param()