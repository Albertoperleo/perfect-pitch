from recognition.pitch import *
import pyaudio
import numpy as np

SAMPLING_RATE = 44100
SAMPLES = 100

def record():
    # Initialize pyaudio
    p = pyaudio.PyAudio()

    # Open stream
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=SAMPLING_RATE,
                    input=True,
                    frames_per_buffer=1024)

    while True:
        # Read stream
        audio_data = stream.read(1024)
        audio_data = np.frombuffer(audio_data, dtype=np.int16)
        
        # Show audio
        show_audio(audio_data, [], SAMPLES)

    # Close stream
    stream.stop_stream()
    stream.close()

    # Finalize pyaudio
    p.terminate()
