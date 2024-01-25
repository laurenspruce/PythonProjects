import pyaudio
import wave
import datetime
import os

#Setting up the parameters
FORMAT = pyaudio.paInt16 #Format of audio samples (16-bit signed integers)
CHANNELS = 1 #Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100 #Sample rate (per second)
CHUNK = 1024 #Number of frames per buffer
RECORD_SECONDS = 5 #Duration of recording in seconds

#Initialise PyAudio object, used for audio input
p = pyaudio.PyAudio()

#Open an audio stream for recording
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

#Recording the audio frames and storing in a list
print("Recording...")

frames = []

for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("Recording finished.")

#Closing the audio stream
stream.stop_stream()
stream.close()

#Terminate the PyAudio object
p.terminate()

#Save the recorded audio to a WAV file
#Adding current timestamp to WAV file to ensure new file doesn't override previous file
current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
filename_with_timestamp = f"output_{current_time}.wav"
WAVE_OUTPUT_FILENAME = os.path.join(r"C:\Users\Lauren\Desktop\Python Projects\audio-recorder", filename_with_timestamp)


wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print(f"Audio saved as {WAVE_OUTPUT_FILENAME}")
