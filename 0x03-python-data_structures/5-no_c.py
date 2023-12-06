#!/usr/bin/python3
def no_c(my_string):
    copied_string = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            copied_string += my_string[i]
    return(copied_string)
