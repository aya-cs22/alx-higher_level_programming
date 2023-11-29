#!/usr/bin/python3
char = 'a'
while char <= 'z':
    if char == 'q' or char == 'e':
        continue
    print(f"{char}".format(char), end="")
    char = chr(ord(char) + 1)
    
