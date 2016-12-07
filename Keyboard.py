import wave
import math
import struct
import pygame
import sys
import random
from pygame.locals import *

samplerate = float(44100)                                                                                   # Hz
SampleLength = 22050                                                                                        # seconds
BitDepth = 32767
envelope_test_values = (0.05, 0.025, 0.4, 0.3)
Soundtuple = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
noise_out = wave.open('keyboard.wav', 'w')
noise_out.setparams(Soundtuple)

values = []


def sound_generator(frequency, envelope_values):
    attack = envelope_values[0] * Soundtuple[2]
    decay = envelope_values[1] * Soundtuple[2]
    sustain = envelope_values[2] * Soundtuple[2]
    release = envelope_values[3] * Soundtuple[2]
    volume = 0.4

    for i in range(0, Soundtuple[3]):
        if i < attack:
            volume += volume / attack
        elif i > attack + decay + sustain:
            volume -= volume - release
        else:
            volume = 1
        if (volume * BitDepth) > BitDepth:
            volume = 1
        value = math.sin(2.0 * math.pi * frequency * i / Soundtuple[2]) * (volume * BitDepth)
        packaged_value = struct.pack('i', value)
        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)

def whitespace():
    for i in range(0, Soundtuple[3]):
        value = math.sin(0)
        packaged_value = struct.pack('i', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)
    value_str = ''.join(values)
    noise_out.writeframes(value_str)


def close_sound():
    noise_out.close()

"Attempting Doubling"
"""def double(list):
    doubled_list = []
    for i in xrange(0, len(list), 2):
        doubled_list.append(list[i])
    values = doubled_list"""

def white_noise():
    for i in xrange(0, Soundtuple[3]):
        noise = random.randrange(-BitDepth, BitDepth)
        packaged_value = struct.pack('i', noise)
        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)




pygame.init()

Width = 800
Height = 600

window = pygame.display.set_mode((Width, Height), 0, 32)

pygame.display.set_caption('Sound Generation Keyboard')
Black = (0, 0, 0)
White = (255, 255, 255)
font = pygame.font.SysFont(None, 96)


while True:
    window.fill(Black)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if keys[K_a]:
            print 'A4'
            sound_generator(440.000, envelope_test_values)
        if keys[K_s]:
            print 'E4'
            sound_generator(493.883, envelope_test_values)

        if keys[K_d]:
            print 'C5'
            sound_generator(523.251, envelope_test_values)

        if keys[K_f]:
            print 'D5'
            sound_generator(587.330, envelope_test_values)

        if keys[K_g]:
            print 'E5'
            sound_generator(659.255, envelope_test_values)

        if keys[K_h]:
            print 'F5'
            sound_generator(698.456, envelope_test_values)

        if keys[K_j]:
            print 'G5'
            sound_generator(783.991, envelope_test_values)

        if keys[K_k]:
            print 'A5'
            sound_generator(880.000, envelope_test_values)

        if keys[K_l]:
            print 'B5'
            sound_generator(987.767, envelope_test_values)

        if keys[K_z]:
            print 'C6'
            sound_generator(1046.50, envelope_test_values)

        if keys[K_x]:
            print 'D6'
            sound_generator(1174.66, envelope_test_values)

        if keys[K_c]:
            print 'E6'
            sound_generator(1318.51, envelope_test_values)

        if keys[K_v]:
            print 'F6'
            sound_generator(1396.91, envelope_test_values)

        if keys[K_b]:
            print 'G6'
            sound_generator(1567.98, envelope_test_valuesfdg)

        if keys[K_SPACE]:
            print 'Silence'
            whitespace()

        if keys[K_BACKSPACE]:
            print 'white noise'
            white_noise()

        if keys[K_RETURN]:
            print 'Sound Closed'
            value_str = ''.join(values)
            noise_out.writeframes(value_str)
            close_sound()
