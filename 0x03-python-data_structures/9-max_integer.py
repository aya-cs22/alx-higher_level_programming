#!/usr/bin/python3
def max_integer(my_list=[]): 
    if (my_list):
        max_num = my_list[0]
        for num in my_list:         #[1, 90, 2, 13, 34, 5, -13, 3]
            if num > max_num:
                max_num = num
        return max_num
    else:
        return None
    
