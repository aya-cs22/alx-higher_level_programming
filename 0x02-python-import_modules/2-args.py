#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    c = len(argv) - 1
    if c == 0:
        print(f"0 arguments.".format(c))
    elif c == 1:
        print(f"1 argument:".format(c))
        print("1: {}".format(argv[1]))
    else:
        print(f"{c} arguments:".format(c))
    for i in range(1,len(argv)):
        print(f"{i}: {argv[i]}".format(i, argv[i]))
