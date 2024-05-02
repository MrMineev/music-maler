from fft import audio_to_function, make_audio
import matplotlib.pyplot as plt
from approximator import get_approximation_for_data
import numpy as np
import wavio as wv

def gen_approx(audio_data, DATA_FREQUENCY = 10, EPS=0.1):
    new_audio_data = []
    for i in range(len(audio_data)):
        if i % DATA_FREQUENCY != 0:
            continue
        new_audio_data.append(audio_data[i])

    gvalue = get_approximation_for_data(new_audio_data)
    print(f"___ INPUT_SIZE = {len(new_audio_data)}, OUTPUT_SIZE = {len(gvalue)} __")

    music_record = []
    for i in range(len(gvalue)):
        for j in range(DATA_FREQUENCY):
            music_record.append(gvalue[i])

    return music_record


