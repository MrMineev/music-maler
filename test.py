from fft import audio_to_function
import matplotlib.pyplot as plt
from approximator import get_approximation_for_data
import numpy as np

EPS = 0.1

audio_data, sample_rate = audio_to_function("records/target.wav")

new_audio_data = []
for i in range(len(audio_data)):
    if i % 1000 != 0:
        continue
    if abs(audio_data[i]) > EPS:
        new_audio_data.append(audio_data[i])

print(new_audio_data)

gvalue = get_approximation_for_data(new_audio_data)

'''

plt.plot([i for i in range(len(gvalue))], gvalue, color='g')
plt.plot([i for i in range(len(audio_data))], audio_data, color='r')
plt.show()

'''

