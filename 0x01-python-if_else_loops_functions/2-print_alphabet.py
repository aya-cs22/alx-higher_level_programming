#!/usr/bin/python3
char = 'a'
while char <= 'z':
    print(f"{char}".format(char) ,end="")
    char = chr(ord (char) + 1)
