#!/usr/bin/python
import sys
def oddeven():
            user_input = raw_input("Enter a number: ")
            try:
                num = int(user_input)
                if (num % 2 == 0):
                    print "The number {} is even".format(num)
                else:
                    print "The number {} is odd".format(num)
            except ValueError:
                print "'{}' is not a number".format(user_input)
while True:
    try:
        oddeven()
    except(EOFError, KeyboardInterrupt):
        print "^D"
        sys.exit(0)