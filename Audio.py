import wave
import struct

Sound = wave.open('noise2.wav','r')
Frames = Sound.getframerate()

for i in range(0, Frames):
    Soundinfo = Sound.readframes(1)
    Soundstruct = struct.unpack("<h",Soundinfo)
    print(int(Soundstruct[0]))

