import wave
import struct
import math

class TextToSpeechEngine:
    def __init__(self, voice_settings):
        self.settings = voice_settings

    def synthesize(self, text):
        return self.generate_wave(text)

    def generate_wave(self, text):
        wave_data = []
        for char in text:
            wave_data.extend(self.sin_wave(char))
        return self.save_wave(wave_data)

    def sin_wave(self, char):
        freq = ord(char) * 10
        length = 8000
        amplitude = 16000
        rate = 44100

        wave = []
        for i in range(length):
            value = math.sin(2.0 * math.pi * freq * (i / rate)) * (amplitude / 2)
            wave.append(int(value))
        return wave

    def save_wave(self, wave_data):
        file = wave.open('output.wav', 'w')
        file.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))
        for value in wave_data:
            packed_value = struct.pack('h', value)
            file.writeframes(packed_value)
        file.close()
        return 'output.wav'

