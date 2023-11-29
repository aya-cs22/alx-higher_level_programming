#!/usr/bin/python3
num1 = 0
num2 =1
while num1 <= 8:
    num2 = 1
    
    while num2 <= 9 :
        if num2 != num1:
            print (num1, end="")
            print (num2, end=", ")
        num2+=1
    num1+=1
