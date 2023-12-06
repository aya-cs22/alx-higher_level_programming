#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if len(i) == 0:
            print("{:d}".format(i), end="")
        else:
            for x in range(len(i)):
                if x == len(i) - 1:
                    print('{:d}'.format(i[x]), end='\n')
                else:
                    print('{:d}'.format(i[x]), end=' ')
