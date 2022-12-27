import matplotlib.pyplot as plt
import numpy as np


def show_audio(audio_data, data, samples):
    """Show the audio figure

    Args:
        audio_data (stream): integer stream with audio data
        data (list): empty list 
    """
    
    data.extend(audio_data)
    
    if len(data) > samples:
            
        # Calculate pitch
        spectrum = calculate_pitch(data, samples)
        
        # Show audio
        plt.plot(spectrum)
        plt.ylim(0,10)
        plt.show(block=False)
        plt.pause(0.01)
        plt.clf()
        plt.xlabel('Frequency')
        plt.ylabel('Amplitude')
        

def calculate_pitch(data, samples):
    """Calculate data's amplitude and frequencies

    Args:
        data (list): samples list
        samples (int): data size
        sampling_rate (int): audio sampling rate

    Returns:
        spectrum(list): frequency spectrum
    """
    
    # DFT data
    data_dft = np.fft.fft(data)
    
    # Amplitude
    spectrum = np.abs(data_dft)
    spectrum = spectrum/samples
    
    return spectrum
    
    