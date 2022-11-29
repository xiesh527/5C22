import wave
import numpy as np
from scipy.io import wavfile
from scipy.interpolate import CubicSpline
#import scipy.io.wavfile
from Median_filter import *
import pandas as pd
import openpyxl
import csv


def main():
    d_samplerate, d_data = wavfile.read('degraded.wav')


    clean_samplerate, clean_data = wavfile.read('myclean.wav')

    file = open('bk.csv')
    csvreader = csv.reader(file)

    rows = []
    for row in csvreader:
        rows.append(row)
    rows
    rows = np.array(rows)
    rows = [int(x) for x in rows]
    bk = rows
    file.close()
    #d_data = d_data
    clean_data = clean_data/32767
    res_data = d_data.copy()

    idx = 6458

    #window = d_data[idx - 3: idx + 4]
    # print(window)

    #filtered = median_fil(window, 3)
    # print(filtered)
    #print(d_data[idx - 3: idx + 4])

    clips_list = np.array([])

    for i in range(len(bk)):
        if(bk[i] == 1):
            clips_list = np.append(clips_list, i)


    clips_list = np.array([int(x) for x in clips_list])

    interesting_slice = d_data[19338 - 3: 19338 + 3 + 1]
    print(interesting_slice)

    filtered = median_fil(interesting_slice, 3)
    print(filtered)

    window_size_lst = f_odd(30)
    MSE_list = np.array([])
    for i in range(len(window_size_lst)):
        window_size = int(window_size_lst[i])
        span = int((window_size - 1) / 2)
        for j in range(len(clips_list)):
            window = d_data[clips_list[j]-span: clips_list[j]+span+1]
            filtered = median_fil(window, window_size)
            res_data[clips_list[j]-span: clips_list[j]+span+1] = filtered
            #print(res_data[clips_list[j]-span: clips_list[j]+span+1])
        normal_res_data = res_data/32767
        MSE = np.square(np.subtract(clean_data, normal_res_data)).mean()
        #print(clean_data[19338 - 3: 19338 + 3 + 1])
        #print(res_data[19338 - 3: 19338 + 3 + 1])
        res_data = d_data.copy()
        MSE_list = np.append(MSE_list, MSE)

    print(MSE_list)
    MSE_data = pd.DataFrame(np.ndarray.tolist(MSE_list.T))
    MSE_data.to_csv('median_data_0.001.csv')
pass

if __name__ == '__main__':
    main()