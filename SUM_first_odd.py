import numpy as np

#This function computes the sum of first odd numbers
def sum_f_odd(N):
    sum = 0
    count = 1
    for i in N:
        sum = sum + (2*count - 1)
        count = count + 1
    return sum