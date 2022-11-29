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
import winsound
from tqdm import tqdm
import matplotlib.pyplot as plt
import unittest


class TestAdd(unittest.TestCase):
    def test_add(self):
        # I do not know to type data like [1 1] in python, hence the result need to be converted to list first
        self.assertEqual(tick_out_clips_index(
            [0, 1, 2, 3, 4, 5], [1, 2]).tolist(), [0, 3, 4, 5])

    def test_check_odd(self):
        self.assertEqual(check_odd(3), 1)

    def test_f_odd(self):
        self.assertEqual(f_odd(3), [1, 3, 5])

    def test_median_fil(self):
        self.assertEqual(median_fil([1, 8, 3], 3), [4, 3, 4])
    # Using mean as the padded number

    def test_get_padding(self):
        self.assertEqual(get_padding(3, [1, 4, 1]), [2, 1, 4, 1, 2])

    def test_report_index(self):
        self.assertEqual(report_index([0, 1, 1, 0]), [1, 2])

    def test_tick_out_clips(self):
        self.assertEqual(
            (tick_out_clips([1, 2], [1, 99, 99, 1])).tolist(), [1, 1])

    def test_tick_out_clips_index(self):
        self.assertEqual(tick_out_clips_index(
            [0, 1, 2, 3, 4, 5], [1, 2]).tolist(), [0, 3, 4, 5])


def main():
    #read in files
    d_samplerate, d_data = wavfile.read('degraded_0.0001.wav')
    d_samplerate1, d_data1 = wavfile.read('degraded.wav')
    clean_samplerate, clean_data = wavfile.read('myclean.wav')
    print('Playing damaged audio')
    #winsound.PlaySound('degraded_0.0001.wav', winsound.SND_FILENAME)
    file = open('bk_0.0001.csv')
    bk = np.zeros(len(d_data))
    # Define variable to read sheet
    csvreader = csv.reader(file)
    normalising_const = 32767

    #Normalise the data in format of 16 bit wav file
    clean_data = clean_data/normalising_const
    d_data1 = d_data/normalising_const
    #obtain the index of each data
    rows = []
    for row in csvreader:
        rows.append(row)
    rows

    rows = np.array(rows)
    rows = [int(x) for x in rows]
    proce_data = d_data1
    for i in range(np.size(d_data1)):
        if (rows[i] == 1):
            print(i)
    window_size = 7
    res_data = d_data.copy()
    restored_data_cubic = d_data.copy()
    bk = rows.copy()
    # sample output generating using Median Filter
    for i in tqdm(range(np.size(d_data))):
        if (rows[i] == 1):
            #prev = d_data[i - 10 : i + 10]
            span = int((window_size - 1) / 2)
            res_data[i - span: i +
                     span + 1] = median_fil(d_data[i - span: i + span + 1], window_length=window_size)
            

    #write results
    filename = 'res.wav'
    wavfile.write(filename, d_samplerate, res_data)
    print("Interpolation completed, Playing restored audio by median filter of window size of 7 at clip density of 0.0001")
    #winsound.PlaySound(filename, winsound.SND_FILENAME)

    clip_idx = report_index(bk)
    window_size_list = f_odd(30)
    window_size_list = np.array([int(x) for x in window_size_list])
    # sample output generating using CSF
    for i in tqdm(range(len(clip_idx))):

        window = locate_window(window_size, clip_idx[i], d_data)
        span = int((window_size - 1) / 2)
        bk_window = bk[clip_idx[i] - span: clip_idx[i] + span + 1]
        window = cubic_interpolation_whole(bk_window, window)
        restored_data_cubic[clip_idx[i] -
                            span: clip_idx[i] + span + 1] = window

    #write results
    filename_cubic = 'cubic_restored.wav'
    wavfile.write(filename_cubic, d_samplerate, restored_data_cubic)
    print("Interpolation completed, Playing restored audio by cubic spline filter of window size of 7 at clip density of 0.0001")
    #winsound.PlaySound(filename_cubic, winsound.SND_FILENAME)
    
    #plot area
    print('Sample output by two filters')
    figure2 = plt.figure(figsize=(8, 10))
    figure2.tight_layout(pad=100.0)
    plt.title('Sample Output from both filters with window length of 7')
    figure2.tight_layout(pad=10.0)
    ax1 = figure2.add_subplot(4, 1, 1)
    ax1.plot(clean_data, label = 'Original')
    plt.legend(loc = "upper left")
    #ax1.set_title("clean")

    ax2 = figure2.add_subplot(4, 1, 2)
    ax2.plot(d_data/normalising_const, label = 'Corrupted')
    plt.legend(loc = "upper left")
    #ax2.set_title("degraded")

    ax3 = figure2.add_subplot(4, 1, 3)
    ax3.plot(res_data/normalising_const, label = 'median')
    #ax3.set_title("restored")
    plt.legend(loc = "upper left")
    ax4 = figure2.add_subplot(4, 1, 4)
    ax4.plot(restored_data_cubic/normalising_const, label = 'cubic')
    #ax4.set_title("cubic")
    plt.legend(loc = "upper left")
    #plt.plot(clean_data)

    figure2.tight_layout(pad=100.0)
    #plt.plot(res_data)
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    
    plt.show()


    print('Two filters performance at density of clip = 0.001 at different window length')
    window_size_axis = f_odd(30)
    window_size_axis = np.delete(window_size_axis, 0)
    print(window_size_axis)

    df = pd.read_csv('cubic_data_0.001.csv')
    # print(df)
    cubic_data = df.to_numpy()
    #print(cubic_data)
    cubic_data = cubic_data[:, 1]
    # print(df)

    df1 = pd.read_csv('median_data_0.001.csv')
    # print(df)
    median_data = df1.to_numpy()
    # print(df)
    median_data = median_data[:, 1]
    median_data = np.delete(median_data, 0)

    cubic_data = np.log10(cubic_data)
    median_data = np.log10(median_data)
    #print(cubic_data)
    plt.plot(window_size_axis, cubic_data, label='cubic spline')
    plt.plot(window_size_axis, median_data, label='median')
    plt.legend(loc="upper left")
    plt.ylabel('Log10 of MSE')
    plt.xlabel('Window size')
    plt.title('Two filters performance under different window length')
    plt.show()


if __name__ == '__main__':

    main()
    unittest.main()
