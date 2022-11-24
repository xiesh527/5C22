import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import csv

d_samplerate, d_data = wavfile.read('degraded.wav')
clean_samplerate, clean_data = wavfile.read('myclean.wav')
res_samplerate, res_data = wavfile.read('res.wav')

d_data = d_data/32767
clean_data = clean_data/32767
res_data = res_data/32767
d_audio = d_data
file = open('bk.csv')
csvreader = csv.reader(file)

rows = []
for row in csvreader:
        rows.append(row)
rows

rows = np.array(rows)
rows = [int(x) for x in rows]
figure, axis = plt.subplots(3)
axis[0].plot(clean_data)
axis[0].set_title("clean")

axis[1].plot(d_data)
axis[1].set_title("degraded")

axis[2].plot(res_data)
axis[2].set_title("restored")

#plt.plot(clean_data)


#plt.plot(res_data)
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()

abs_d = np.abs(d_data)
abs_clean = np.abs(clean_data)
abs_res = np.abs(res_data)

figure, axis = plt.subplots(3)
axis[0].plot(abs_clean)
axis[0].set_title("clean")

axis[1].plot(abs_d)
axis[1].set_title("degraded")

axis[2].plot(abs_res)
axis[2].set_title("restored")


plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()

MSE = np.square(np.subtract(clean_data, res_data)).mean()
print(MSE)

MSE1 = np.square(np.subtract(clean_data, d_data)).mean()
print(MSE1)