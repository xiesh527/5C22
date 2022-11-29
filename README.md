# Add here a title for the project

## Table of Content
1.[High-level Description of the project](#my-first-title)
1.[Installation and Execution](#my-second-title)
1.[Methodology and Results](#my-third-title)
1.[Credits](#my-fourth-title)
## High-level Description of the project
This assignment builds on Assignment I. 
Which code could be found at: 
We assume that we have successfully detected the clicks and we are applying different interpolation methods to restore the audio, such as
- median filtering
- cubic splines

Using the detected clips index as a prior knowledge, both filters were applied to the deraged signal. This project mainly studied their performance under different window sizes, and also under the noise level of signal, which is quantified as the density of clips existed in the degraded audio.

1) Median Filter:
    Median filter would sort the whole sequence in order of magnitude, obtain the middle element i.e. Median(which requires an odd number of data points), and replace the detected clips by the median. Its logic could be intuitively written as:
    '''
    for data in signal:
        window = signal[sequence(data) - span : sequence(data) + span]#span is half of (window's length - 1)
        S_window = sort(window)
        m_value = median(S_window)
        data = m_value
---

## Installation and Execution

Provide details on the Python version and libraries (e.g. numpy version) you are using. One easy way to do it is to do that automatically:
```sh                                 
pip3 install pipreqs

pipreqs $project/path/requirements.txt
```
For more details check [here](https://github.com/bndr/pipreqs)


Afer installing all required packages you can run the demo file simply by typing:
```sh
python demo_audio_restoration.py
```
---

## Methodology and Results
Describe here how you have designed your code, e.g. a main script/routine that calls different functions, is the unittesting included in the main routine? 



**Results**

1. For the median filter, different lengths were explored to test the effectiveness of the restoration. In particular, XXXX were tested and XXX was observed to deliver the lowest MSE, as shown in the figure below.

<img src="MedianFilter_MSEvsLength.png" width="350">

The restored waveform <output_medianFilter.wav> with the optimal filter length is given below:



2. Using the cubic splines, we observe ....

The restored waveform <output_cubicSplines.wav> with the optimal filter length is given below:


3. Comparing the two different interpolation methods, we notice that method X achieves a lower MSE. The runtime of XX method is .....

After listening to the two restored files, we notice ...


---
## Credits

This code was developed for purely academic purposes by XXXX (add github profile name) as part of the module ..... 

Resources:
- XXXX
- XXX





