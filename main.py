from gen import gen_approx
from fft import audio_to_function, make_audio
import numpy as np
import matplotlib.pyplot as plt

K = 50000

audio_data, sample_rate = audio_to_function("records/target.wav")
split_arrays = np.array_split(np.array(audio_data), K)
result = []
index = 0
for mas in split_arrays:
  print(index)
  index += 1
  music = gen_approx(mas)
  result.extend(music)

plt.plot([i for i in range(len(audio_data))], audio_data, 'o', label='Data points')
plt.plot([i for i in range(len(audio_data))], audio_data, label='Actual g(x)')
plt.plot([i for i in range(len(result))], result, label='Approximated g(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Function Approximation using Least Squares Regression')
plt.show()

make_audio(result)
