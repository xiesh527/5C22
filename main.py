import numpy as np
from MSE import *
from SUM_first_odd import *
Y_pred = np.array([2, 2, 2, 2])
Y_act = np.array([1, 1, 1, 1])

mse = MSE(Y_pred, Y_act)

print(mse)

sum = sum_f_odd(3)
print(sum)