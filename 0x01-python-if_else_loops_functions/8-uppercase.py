#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            result += chr(ord(i) - ord('a') + ord ('A'))
        else:
            result += i
    print(f"{result}".format(result))
