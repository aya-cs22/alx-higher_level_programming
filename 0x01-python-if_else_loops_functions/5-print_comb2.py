#!/usr/bin/python3
num = 0
while num < 100:
    print(f"{str(num).zfill(2)}".format(num))
    num += 1
