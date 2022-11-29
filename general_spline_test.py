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

arr = [2, 3, 14, 6, 9999, 2, 9999, -3, 45]
bk = [0, 0, 0, 0, 1, 0, 1, 0, 0]

#print(cubic_interpolation_loc_general(arr))