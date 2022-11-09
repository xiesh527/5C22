import numpy as np

def sum_f_odd(N):
    sum = 0
    for i in N:
        sum = sum + (2*i - 1)
    return sum