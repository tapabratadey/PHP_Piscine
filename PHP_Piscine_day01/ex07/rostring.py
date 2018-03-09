#!/usr/bin/python
import sys
def rostring():
    if len(sys.argv) == 1:
        sys.exit(0)
    place = 1
    store = sys.argv[1].split()
    count = len(store)
    myList = []
    while (place < count):
        myList.append(store[place])
        place += 1 
    if (myList == [""]):
        print ""
        sys.exit(0)
    try:
        myList.append(store[0])
        print (' '.join(myList))
    except IndexError:
        print ("")
rostring()