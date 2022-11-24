import wave
import numpy as np
from scipy.io import wavfile
#import scipy.io.wavfile
from Median_filter import *
import pandas as pd
import openpyxl
import csv


d_samplerate, d_data = wavfile.read('degraded.wav')
clean_samplerate, clean_data = wavfile.read('myclean.wav')
file = open('bk1.csv')
bk = np.zeros(len(d_data))
# Define variable to read sheet
csvreader = csv.reader(file)
d_data = d_data
clean_data = clean_data

rows = []
for row in csvreader:
        rows.append(row)
rows

rows = np.array(rows)
window_size = 3
res_data = d_data
rows = [int(x) for x in rows]
for i in range(np.size(d_data)):
        if (rows[i] == 1):
            prev = d_data[i - 10 : i + 10]
            
            res_data[i - 10 : i + 10] = median_fil(d_data[i - 10 : i + 10], window_length=window_size)
            after = res_data[i - 10 : i + 10]
            #print(prev)
            #print(after)
filename = 'res.wav'
wavfile.write(filename, d_samplerate, res_data)




