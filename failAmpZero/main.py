import numpy as np
import wave

def find_z_cross(signal):
    z_cross = np.where(np.diff(np.sign(signal)))[0]  # Find 0 cross
    return z_cross

def encode_amplitude_zero_crossing(input_wav, output_wav, secret_message):
    with wave.open(input_wav, 'rb') as song:    #load wav
        params = song.getparams()
        n_frames = song.getnframes()
        frames = song.readframes(n_frames)
        
        audio = np.frombuffer(frames, dtype=np.int16).copy() #stupid readable permissions

    secret_message += '0000000000'  # Delimiter to indicate end of message
    b_msg = ''.join([format(ord(char), '08b') for char in secret_message]) #binary
    print(b_msg)
    
    z_cross = find_z_cross(audio)

    for i in range(min(len(b_msg), len(z_cross))):  #for 0crossings
        cross = z_cross[i]
        bit = int(b_msg[i])
        print(audio[cross])
        if bit == 1:
            audio[cross] += 10000  # Larger change for '1'
        else:
            audio[cross] -= 10000  # Larger change for '0'


    modified_frames = audio.tobytes()
    with wave.open(output_wav, 'wb') as output_song:
        output_song.setparams(params)
        output_song.writeframes(modified_frames)

    print(f"Message encoded")

def decode_amplitude_zero_crossing(stego_wav):
    with wave.open(stego_wav, 'rb') as song:
        n_frames = song.getnframes()
        frames = song.readframes(n_frames)
        
        # Convert numpy array
        audio = np.frombuffer(frames, dtype=np.int16)

    z_cross = find_z_cross(audio)

    extracted_bin = []
    for cross in z_cross:
        # 25 threshold?
        if audio[cross] > 5000:  # 1
            extracted_bin.append('1')
        elif audio[cross] < -5000:  # 0
            extracted_bin.append('0')

    #Convert binstr
    extracted_bin_str = ''.join(extracted_bin)
    print(extracted_bin_str)
    decoded_message = ''.join([chr(int(extracted_bin_str[i:i+8], 2)) for i in range(0, len(extracted_bin_str), 8)])
    
    decoded_message = decoded_message.split('###')[0]   #Stop decoding ###

    print(f"Decoded message: {decoded_message}")
    return decoded_message

encode_amplitude_zero_crossing('input.wav', 'output.wav', 'secret')
decode_amplitude_zero_crossing('output.wav')
