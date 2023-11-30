#!/usr/bin/python3
def uppercase(str):
    for word in str:
        if (str != " " or str != ","):
            print(f"{str.capitalize()}".format(str))
