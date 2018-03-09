#!/usr/bin/python
import sys
def ssap():
    if len(sys.argv) == 1:
        sys.exit(0)
    arg = len(sys.argv) - 1
    place = 1
    argStr = ""
    while (place <= arg):
        argStr += sys.argv[place] + " "
        place += 1
    words = argStr.split()
    words.sort()
    print '\n'.join(words)
ssap()