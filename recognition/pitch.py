from recognition.note_freq import NOTE_FREQUENCIES
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
        note = calculate_note(spectrum)
        print(max(spectrum))
        print(note)
        
        # Show audio with log expression
        plt.plot(10*np.log10(spectrum))
        plt.show(block=False)
        plt.pause(0.5)
        plt.clf()
        plt.title(note)
        plt.xlabel('Freq. (Hz)')
        plt.ylabel('Pot. (dB)')
        

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
    
    # Spectrum
    spectrum = np.abs(data_dft)
    spectrum = spectrum/samples
    
    # Logaritmic expression
    spectrum = spectrum**2
    
    return spectrum


def calculate_note(spectrum):
    
    note = 'None'
    note_max = max(spectrum)
    freq_values = NOTE_FREQUENCIES.values()
    
    if note_max >= min(freq_values):
        for k,v in NOTE_FREQUENCIES.items():
            cont = 0
            while(note_max/2 >= min(freq_values)):
                cont += 1
                note_max = note_max / 2
            if note_max >= v-0.5 and note_max <= v-0.5:
                note = k[0] + str(cont)
                
    return note
        
    