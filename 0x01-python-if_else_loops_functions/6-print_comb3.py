#!/usr/bin/python3
num1 = 0
num2 =1
while num1 <= 8:
    num2 = 1
    while num2 <= 9 :
            if num2 > num1 and num1 + num2 == 17:
                print (f"{num1}".format(num1), end="")
                print (f"{num2}".format(num2), end=", ")
            num2+=1
    num1+=1
    print("89")
