import numpy as np

def median_fil(
    signal, 
    window_length):
    filtered = []
    if check_odd(window_length) == 1:
        padded_signal = get_padding(window_length, signal)
        #print(padded_signal)
        for i in range(len(signal)):
            #print(i)
            window = padded_signal[i:i+window_length]
            window = np.sort(window)
            median_item = window[int((window_length-1)/2)]
            
            filtered = np.append(filtered, median_item)
    else:
        print("Window length not valid(odd)")
    return filtered
def check_odd(
    number
    ):
    if number%2 == 1:
        return 1
    else:
        return 0

def get_padding(
    number, signal
    ):
    padding_length = int((number - 1)/2)
    
    padding = np.zeros(padding_length)

    signal = np.append(padding, signal)
    signal = np.append(signal, padding)

    return signal


def f_odd(N):
    odd_list = np.array([])
    count = 1
    for i in range(N):
        curr_odd = 2*count - 1
        count = count + 1
        odd_list = np.append(odd_list, curr_odd)
    return odd_list