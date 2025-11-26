#!/usr/bin/python3
import sys
argv = sys.argv[1:]
count = len(argv)
if __name__ == "__main__":
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))

    if count > 0:
        for i, arg in enumerate(argv):
            position = i + 1
            print("{}: {}".format(position, arg))
