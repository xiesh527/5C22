import numpy as np
from scipy.io import wavfile
from scipy.interpolate import CubicSpline


def report_index(bk):
    clip_index = np.array([])
    for i in range(len(bk)):
        if(bk[i] == 1):
            clip_index = np.append(clip_index, i)
    clip_index = [int(x) for x in clip_index]
    return clip_index


def tick_out_clips(index_list, signal):

    ticked_signal = np.delete(signal, index_list)
    return ticked_signal


def tick_out_clips_index(x, index_list):
    x_ticked = np.delete(x, index_list)
    return x_ticked


def cubic_interpolation_whole(bk, signal):
    x_axis = np.linspace(0, len(bk)-1, len(bk))
    # print(x_axis)
    clip_index = report_index(bk)
    ticked_signal = tick_out_clips(clip_index, signal)
    ticked_x = tick_out_clips_index(x_axis, clip_index)
    # print(ticked_signal)
    # print(ticked_x)

    res_cubic = CubicSpline(ticked_x, ticked_signal)
    res_cubic_signal = res_cubic(x_axis)
    res_cubic_signal = np.array(res_cubic_signal)
    # print(res_cubic_signal)
    return res_cubic_signal


def cubic_interpolation_loc(window_size, signal):
    x_axis = np.linspace(0, len(signal)-1, len(signal))
    # print(x_axis)
    clip_index = int((window_size - 1) / 2)
    ticked_signal = tick_out_clips(clip_index, signal)
    ticked_x = tick_out_clips_index(x_axis, clip_index)
    # print(ticked_signal)
    # print(ticked_x)

    res_cubic = CubicSpline(ticked_x, ticked_signal)
    res_cubic_signal = res_cubic(x_axis)
    res_cubic_signal = np.array(res_cubic_signal)
    # print(res_cubic_signal)
    return res_cubic_signal





def locate_window(window_size, clip_idx, signal):
    if(window_size % 2 == 0):
        print("Window size not valid")
    span = int((window_size - 1) / 2)
    # print(span)
    signal_slice = signal[clip_idx - span: clip_idx + span + 1]
    return signal_slice
