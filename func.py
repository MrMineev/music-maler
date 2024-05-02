import numpy as np
from fft import audio_to_function

class MusicFunc:
  def __init__(self, N=3):
    self.N = N

    self.data = []
    for i in range(N):
      audio_data, sample_rate = audio_to_function(f"my_recordings/record_{i+1}.wav")
      self.data.append(audio_data)

  def super_f(self, index, x):
    return self.data[index][x]


