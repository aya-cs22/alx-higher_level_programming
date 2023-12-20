#!/usr/bin/python3
def safe_print_integer(value):
    value = 0
    if isinstance(value, int):
       try:
           print("{}".format(value), end="")
        except:
           print("{} is not an integer".format(value), end="")
           
            
