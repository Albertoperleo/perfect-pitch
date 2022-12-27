import pyaudio
import wave

def record():
    # Inicializar PyAudio
    p = pyaudio.PyAudio()

    # Abrir stream de audio
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)

    # Bucle infinito para leer el stream de audio
    while True:
        # Leer datos del stream
        data = stream.read(1024)
        
        print(data)

        # Procesar datos del stream
        # ...

    # Cerrar stream de audio
    stream.stop_stream()
    stream.close()

    # Finalizar PyAudio
    p.terminate()
