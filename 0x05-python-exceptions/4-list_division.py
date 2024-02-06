#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    res = 0
    i = 0
    while i < list_length:
        try:
            res = my_list_1 / my_list_2
        except ZeroDivisionError:
            res = "division by 0"
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(res)
    return(new_list)
