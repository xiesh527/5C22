import numpy as np
from sklearn.metrics import mean_squared_error
from MSE import *
from SUM_first_odd import *
Y_pred = np.array([1, 3, 5, 7, 9])
Y_act = np.array([2, 4, 6, 8, 10])

mse = MSE(Y_act, Y_pred)
test_mse = mean_squared_error(Y_act, Y_pred)
print("MSE is")
print(mse)
print("Validation MSE using builting function is")
print(test_mse)
if test_mse == mse:
    print("MSE working")


sum = sum_f_odd(5)

test_sum = np.sum([1, 3, 5, 7, 9])
print("The sum of the first 5 odd numbers is")
print(sum)
print("Validation sum by explicitly defining first 5 odd number is")
print(test_sum)
if test_sum == sum:
    print("Odd function working")
