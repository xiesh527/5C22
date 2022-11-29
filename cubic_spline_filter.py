import wave
import numpy as np
from scipy.io import wavfile
from scipy.interpolate import CubicSpline
#import scipy.io.wavfile
from Median_filter import *
import pandas as pd
import openpyxl
import csv


d_samplerate, d_data = wavfile.read('degraded.wav')
d_samplerate1, d_data1 = wavfile.read('degraded.wav')
clean_samplerate, clean_data = wavfile.read('myclean.wav')
file = open('bk.csv')
bk = np.zeros(len(d_data))
# Define variable to read sheet
csvreader = csv.reader(file)
clean_data = clean_data
d_data1 =d_data
rows = []
for row in csvreader:
        rows.append(row)
rows

rows = np.array(rows)
rows = [int(x) for x in rows]
proce_data = d_data1


x = np.arange(0, len(d_data)/d_samplerate, 1 /d_samplerate)

res_cubic = CubicSpline(x, proce_data)
res_cubic_signal = res_cubic(x)
res_cubic_signal = np.array(res_cubic_signal)

filename1 = 'cubic_res.wav'
wavfile.write(filename1, d_samplerate, res_cubic_signal)