#!/usr/bin/python3
num = 0
while num < 100:
    if num != None: 
        print(f"{str(num).zfill(2)}".format(num), end =", ")
        num += 1
