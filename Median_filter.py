import numpy as np


def median_fil(
        signal,
        window_length):
    filtered = []

    if check_odd(window_length) == 1:
        padded_signal = get_padding(window_length, signal)
        # print(padded_signal)
        for i in range(len(signal)):
            # print(i)
            window = padded_signal[i:i+window_length]
            window = np.sort(window)
            median_item = window[int((window_length-1)/2)]

            filtered = np.append(filtered, median_item)
    else:
        print("Window length not valid(odd)")
    filtered = [int(x) for x in filtered]
    #filtered = np.array(filtered)
    return filtered





def check_odd(
    number
):
    if number % 2 == 1:
        return 1
    else:
        return 0


def get_padding(
    number, signal
):
    padding_length = int((number - 1)/2)
    mean = np.mean(signal)
    #sorted_signal = np.sort(signal)
    #median_item = sorted_signal[padding_length]
    padding = np.zeros(padding_length)
    padding = padding + mean
    signal1 = np.append(padding, signal)
    signal1 = np.append(signal1, padding)
    signal1 = [int(x) for x in signal1]
    return signal1


def f_odd(N):
    odd_list = np.array([])
    count = 1
    for i in range(N):
        curr_odd = 2*count - 1
        count = count + 1
        odd_list = np.append(odd_list, curr_odd)
    
    
    odd_list = [int(x) for x in odd_list]
    #odd_list = np.array(odd_list)
    return odd_list



