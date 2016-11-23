import wave
import math
import struct

Sound = wave.open('Speaking4lyf.wav','r')
Frames = Sound.getframerate()
samplerate = float(44100) # Hz
SampleLength = 44100 * 4 # seconds
frequency = 440 # Hz
amplitude = 0.5
BitDepth = 32767


Soundtuple = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
noise_out = wave.open('noise2.wav','w')
noise_out.setparams(Soundtuple)

values = []

for i in range(0, Soundtuple[3]):
    value = math.sin(2.0 * math.pi * frequency * (i/Soundtuple[2])) * (amplitude * BitDepth)
    print value

    if Soundtuple[3] > 66150:
        value += math.sin(2.0 * math.pi * 0.05 * frequency * (66150 / Soundtuple[2])) * (0.9 * amplitude * BitDepth)

    packaged_value = struct.pack('h', value)

    for j in xrange(0,Soundtuple[0]):
        values.append(packaged_value)

value_str = ''.join(values)
noise_out.writeframes(value_str)

noise_out.close()