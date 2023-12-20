#!/usr/bin/python3o
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
            i += 1
            continue
        except TypeError:
            new_list.append(0)
            print("wrong type")
            i += 1
            continue
        except IndexError:
            new_list.append(0)
            print("out of range")
            i += 1
            continue
        finally:
            pass
    return new_list
        
