#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from sys import argv
    c = len(sys.argv) - 1
    if c == 0:
        print(f"{c} argument".format(c))
    else:
        print(f"{c} arguments".format(c))
    for i in range(sys.argv):
        print(f"{i} {sys.argv[i]}".format(i, sys.argv[i]))
