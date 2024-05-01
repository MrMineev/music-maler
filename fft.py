import matplotlib.pyplot as plt
from sympy import ifft
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import librosa

freq = 44100

def get_fft(data):
    return np.fft.ifft(data)

def get_ifft(data):
    return np.fft.ifft(data)

def make_audio(data):
    wv.write("result.wav", data, freq, sampwidth=2)

def audio_to_function(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    return y, sr

