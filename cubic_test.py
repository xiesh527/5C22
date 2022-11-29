import wave
import numpy as np
from scipy.io import wavfile
from scipy.interpolate import CubicSpline
#import scipy.io.wavfile
from Median_filter import *
from cubic_spline_fil import *
import pandas as pd
import openpyxl
import csv


def main():

    d_samplerate, d_data = wavfile.read('degraded.wav')

    clean_samplerate, clean_data = wavfile.read('myclean.wav')

    clean_data = clean_data
    d_data = d_data/32767
    clean_data = clean_data/32767
    file = open('bk.csv')
    bk = np.zeros(len(d_data))
    # Define variable to read sheet
    csvreader = csv.reader(file)
    clean_data = clean_data
    d_data1 = d_data
    rows = []
    for row in csvreader:
        rows.append(row)
    rows

    rows = np.array(rows)
    rows = [int(x) for x in rows]

    # print(rows)
    bk = rows
    restored_data = d_data.copy()
    restored_data_1 = d_data.copy()
    clip_idx = report_index(bk)
    window_size_list = f_odd(30)
    window_size_list = np.array([int(x) for x in window_size_list])
    # for i in range(len(clip_idx)):
    #  print(clip_idx[i])
    # print(bk[369159])

    for i in range(len(clip_idx)):

        window = locate_window(window_size_list[8], clip_idx[i], d_data)

        span = int((window_size_list[8] - 1) / 2)
        bk_window = bk[clip_idx[i] - span: clip_idx[i] + span + 1]
        window = cubic_interpolation_whole(bk_window, window)
        restored_data[clip_idx[i] - span: clip_idx[i] + span + 1] = window

    #filename = 'cubic_restored_r.wav'
    # print(type(restored_data[1]))
    wavfile.write('cubic_restored_r.wav', d_samplerate,
                  restored_data.astype(np.float32))
    MSE_list = np.array([])
    window_size_list = np.delete(window_size_list, 0)
    # print(window_size_list)

    for i in range(len(window_size_list)):
        window_size = window_size_list[i]

        for j in range(len(clip_idx)):
            window = locate_window(window_size, clip_idx[j], d_data)

            # print(window)
            span = int((window_size - 1) / 2)
            bk_window = bk[clip_idx[j] - span: clip_idx[j] + span + 1]
            window = cubic_interpolation_whole(bk_window, window)
            restored_data_1[clip_idx[j] - span: clip_idx[j] + span + 1] = window
    # print(restored_data_1[574733])
        MSE = np.square(np.abs(np.subtract(clean_data, restored_data_1))).mean()
        MSE_list = np.append(MSE_list, MSE)

    print(MSE_list)
    res = cubic_interpolation_whole(bk, d_data)
    MSE_whole = np.square(np.abs(np.subtract(clean_data, res))).mean()
    print('MSE while taking whole signal as the window')
    print(MSE_whole)

    MSE_data = pd.DataFrame(np.ndarray.tolist(MSE_list.T))
    MSE_data.to_csv('cubic_data_0.001.csv')
    pass


if __name__ == '__main__':
    main()
