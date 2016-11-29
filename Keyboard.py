import wave
import math
import struct
import pygame
import sys
from pygame.locals import *

samplerate = float(44100) # Hz
SampleLength = 11025# seconds
frequency = 440 # Hz
amplitude = 0.8
samples = frequency*samplerate
BitDepth = 32767
Soundtuple = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
Soundtuple2 = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
Soundtuple3 = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
Soundtuple4 = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
Soundtuple5 = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
noise_out = wave.open('keyboard.wav','w')
noise_out.setparams(Soundtuple)

values = []
def A4():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 440.000 * (i/Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def B4():
    for i in range(0, Soundtuple2[3]):
        value = math.sin(2.0 * math.pi * 493.883 * (i/Soundtuple2[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple2[0]):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.writeframes(value_str)

def C5():
    for i in range(0, Soundtuple3[3]):
        value = math.sin(2.0 * math.pi * 523.251 * (i/Soundtuple3[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple3[0]):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.writeframes(value_str)

def D5():
    for i in range(0, Soundtuple4[3]):
        value = math.sin(2.0 * math.pi *  587.330 * (i/Soundtuple4[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple4[0]):
            values.append(packaged_value)

def E5():
    for i in range(0, Soundtuple5[3]):
        value = math.sin(2.0 * math.pi *  659.255 * (i / Soundtuple5[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple5[0]):
            values.append(packaged_value)

def F5():
    for i in range(0, Soundtuple5[3]):
        value = math.sin(2.0 * math.pi *  698.456 * (i / Soundtuple5[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple5[0]):
            values.append(packaged_value)

def G5():
    for i in range(0, Soundtuple5[3]):
        value = math.sin(2.0 * math.pi *  783.991 * (i / Soundtuple5[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple5[0]):
            values.append(packaged_value)

def E6():
    for i in range(0, Soundtuple5[3]):
        value = math.sin(2.0 * math.pi * 1318.51 * (i / Soundtuple5[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple5[0]):
            values.append(packaged_value)

def B5():
    for i in range(0, Soundtuple5[3]):
        value = math.sin(2.0 * math.pi * 987.767 * (i / Soundtuple5[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple5[0]):
            values.append(packaged_value)

def C6():
    for i in range(0, Soundtuple5[3]):
        value = math.sin(2.0 * math.pi * 1046.50 * (i / Soundtuple5[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple5[0]):
            values.append(packaged_value)

def D6():
    for i in range(0, Soundtuple5[3]):
        value = math.sin(2.0 * math.pi * 1174.66 * (i / Soundtuple5[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple5[0]):
            values.append(packaged_value)

def A5():
    for i in range(0, Soundtuple5[3]):
        value = math.sin(2.0 * math.pi * 880.000 * (i / Soundtuple5[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple5[0]):
            values.append(packaged_value)

def F6():
    for i in range(0, Soundtuple5[3]):
        value = math.sin(2.0 * math.pi * 1396.91 * (i / Soundtuple5[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple5[0]):
            values.append(packaged_value)

def A6():
    for i in range(0, Soundtuple5[3]):
        value = math.sin(2.0 * math.pi * 1760.00 * (i / Soundtuple5[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple5[0]):
            values.append(packaged_value)

def G6():
    for i in range(0, Soundtuple5[3]):
        value = math.sin(2.0 * math.pi * 1567.98 * (i / Soundtuple5[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple5[0]):
            values.append(packaged_value)

def Whitespace():
    for i in range(0, Soundtuple[3]):
        value = math.sin(0)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
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
    pygame.key.set_repeat(5000, 5000)
    window.fill(Black)
    keys = pygame.key.get_pressed()

    if keys[K_a]:
        print 'A4'
        A4()

    if keys[K_s]:
        print 'E4'
        B4()

    if keys[K_d]:
        print 'C5'
        C5()

    if keys[K_f]:
        print 'D5'
        D5()

    if keys[K_g]:
        print 'E5'
        E5()

    if keys[K_h]:
        print 'F5'
        F5()

    if keys[K_j]:
        print 'G5'
        G5()

    if keys[K_k]:
        print 'A5'
        A5()

    if keys[K_l]:
        print 'B5'
        B5()

    if keys[K_z]:
        print 'C6'
        C6()

    if keys[K_x]:
        print 'D6'
        D6()

    if keys[K_x]:
        print 'E6'
        E6()

    if keys[K_c]:
        print 'F6'
        F6()

    if keys[K_v]:
        print 'G6'
        G6()

    if keys[K_SPACE]:
        print 'Silence'
        Whitespace()

    if keys[K_RETURN]:
        print 'Sound Closed'
        CloseSound()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
