import pyaudio
import wave

class Recorder:
    def record(seconds=1):
        CHUNK = 1000
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000

        p = pyaudio.PyAudio()

        # Set listen settings
        stream = p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK
        )

        print("start recording")

        # record for a few seconds
        frames = []
        for i in range(0, int(RATE / CHUNK * seconds)):
            data = stream.read(CHUNK)
            frames.append(data)

        # shutdown stream
        print("recording stopped")
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Save recording
        wf = wave.open("output.wav", 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()