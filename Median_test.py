import numpy as np
import scipy
from Median_Filter import *


arrld = np.array([1, 2, 3, 6, 10, 7, 2, 1])
print(arrld)
print(arrld.shape)

window_size = 3
filtered_signal_hm = np.array([int(x) for x in median_fil(arrld, window_size)])

filtered_signal_sci = scipy.signal.medfilt(arrld, kernel_size = window_size)

print(filtered_signal_hm)
print(filtered_signal_sci)
print(type(filtered_signal_hm))

print(type(filtered_signal_sci))

if (filtered_signal_hm.all() == filtered_signal_sci.all()):
    print("Have the same output to scipy")
    print("Mission Accomplished")

