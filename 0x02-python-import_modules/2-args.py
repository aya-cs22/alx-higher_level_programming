#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = len(argv) - 1
    if (c == 0):
        print("0 arguments.")
    elif (c == 1):
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(len(argv)))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
