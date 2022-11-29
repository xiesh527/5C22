import wave
import numpy as np
from scipy.io import wavfile

from Median_filter import *

text_file = open("bk.txt", "r")
bk = np.array(text_file.read().split(',')).astype(int)

d_samplerate, d_data = wavfile.read('degraded.wav')
clean_samplerate, clean_data = wavfile.read('myclean.wav')
#print(d_samplerate)
#print(np.size(d_data))
#print(np.size(clean_data))
#print(bk)
d_data = d_data/32767
clean_data = clean_data/32767
#print(d_data)
res_data = d_data
window_size = 21

odd_list = [int(x) for x in f_odd(15)]
MSE_list = []


for j in range(len(odd_list)):

    window_size = odd_list[j]
    span = int((window_size - 1) / 2)
    for i in range(np.size(d_data)):
        if (bk[i] == 1):
            res_data[i - span : i + span] = median_fil(d_data[i - span : i + span], window_length=window_size)
            #print(res_data[i - 10 : i + 10])
            #print(np.size(res_data[i - 10 : i + 10]))
            print(i)

    MSE = np.square(np.subtract(clean_data, res_data)).mean()
    MSE_list = np.append(MSE_list, MSE)


print(MSE_list)


