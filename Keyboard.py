import wave
import math
import struct
import pygame
import sys
from pygame.locals import *

samplerate = float(44100) # Hz
SampleLength = 22050# seconds
frequency = 440 # Hz
amplitude = 1
samples = frequency*samplerate
BitDepth = 32767
Soundtuple = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
Soundtuple2 = (1, 2, samplerate*2, SampleLength, 'NONE', 'Not compressed')
Soundtuple3 = (1, 2, samplerate*3, SampleLength, 'NONE', 'Not compressed')
Soundtuple4 = (1, 2, samplerate*4, SampleLength, 'NONE', 'Not compressed')
noise_out = wave.open('noise3.wav','w')
noise_out.setparams(Soundtuple)

values = []
def Sound1():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * frequency * (i/Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def Sound2():
    for i in range(0, Soundtuple2[3]):
        value = math.sin(2.0 * math.pi * frequency/1.3 * (i/Soundtuple2[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple2[0]):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.writeframes(value_str)

def Sound3():
    for i in range(0, Soundtuple3[3]):
        value = math.sin(2.0 * math.pi * frequency/2.4 * (i/Soundtuple3[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple3[0]):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.writeframes(value_str)

def Sound4():
    for i in range(0, Soundtuple4[3]):
        value = math.sin(2.0 * math.pi * frequency*2 * (i/Soundtuple4[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple4[0]):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.writeframes(value_str)

def CloseSound():
    noise_out.close()


pygame.init()

Width = 800
Height = 600

window = pygame.display.set_mode((Width, Height), 0, 32)

pygame.display.set_caption('Sound Generation')
Black = (0, 0, 0)
White = (255, 255, 255)
font = pygame.font.SysFont(None, 96)


while True:

    window.fill(Black)
    keys = pygame.key.get_pressed()

    if keys[K_a]:
        print 'Sound one working'
        Sound1()

    if keys[K_s]:
        print 'Sound two working'
        Sound2()

    if keys[K_d]:
        print 'Sound three working'
        Sound3()

    if keys[K_f]:
        print 'Sound four working'
        Sound4()

    if keys[K_RETURN]:
        CloseSound()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
