import numpy as np
import librosa
from scipy.fftpack import fft

def decode_message(audio_file, message_length):
    audio, sr = librosa.load(audio_file, sr=None)   #Librosa load

    #frames
    f_size = len(audio) // message_length
    frames = [audio[i:i + f_size] for i in range(0, len(audio), f_size)]    

    decode_bits = []
    for i, frame in enumerate(frames[:message_length]):
        fft_frame = fft(frame)  #fft the frame
        
        real_part = np.real(fft_frame[0])   #get real part
        print(real_part)

        if real_part > 5000:  #detection
            decode_bits.append('1')
        else:
            decode_bits.append('0')

    print(decode_bits)

    decoded_message = ''.join([chr(int(''.join(decode_bits[i:i+8]), 2)) for i in range(0, len(decode_bits), 8)])
    
    return decoded_message.split(chr(0))[0]

encoded_audio = "out.wav"
message_length = 40 
decoded_message = decode_message(encoded_audio, message_length)
print("Decoded Message:", decoded_message)
