#!/usr/bin/python
import sys
def epur_str():
    if len(sys.argv) != 2:
        sys.exit(0)
    arg = str(sys.argv[1])
    word = ' '.join(arg.split())
    print word
epur_str()