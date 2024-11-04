import numpy as np
import librosa
from scipy.fftpack import fft, ifft
import soundfile as sf

def encode_message(audio_file, output_file, message):
    audio, sr = librosa.load(audio_file, sr=None)   #Librosa load

    # Message processing
    message += chr(0)  # Append a null term for msg end
    encode_bits = ''.join([f'{ord(c):08b}' for c in message])  #message to bin
    print(f"Binary Message: {encode_bits}")
    print(len(encode_bits))
    
    frame_size = len(audio) // len(encode_bits)    # frame conversion
    frames = [audio[i:i + frame_size] for i in range(0, len(audio), frame_size)]

    for i, frame in enumerate(frames[:len(encode_bits)]):
        fft_frame = fft(frame)  #fft frames

        if encode_bits[i] == '1':
            for j in range(len(fft_frame.real)):    #changing entire frequency of the frame
                fft_frame.real[j] += 10000  #bigger shift?

        # inverse FFT
        frames[i] = np.real(ifft(fft_frame))

    modified_audio = np.hstack(frames)    # Recombine the chunks back into the audio signal
    sf.write(output_file, modified_audio, sr)   # Write the modified to new file

    print(f"Message encoded, saved as {output_file}")

audio_file = "input.wav"
output_file = "output.wav"
message = "TEST"
encode_message(audio_file, output_file, message)
