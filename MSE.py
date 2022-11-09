import numpy as np

def MSE(y_hat, y_o):
    diff_list = (y_hat - y_o)
    squared_diff = diff_list.T * diff_list
    MSE = np.mean(squared_diff)
    return MSE