#!/usr/bin/python3
num = 0
while num < 100:
    if (num != 99):
        print(f"{str(num).zfill(2)}".format(num), end=", ")
    num += 1
print("99")
