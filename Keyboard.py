import wave
import math
import struct
import pygame
import sys
from pygame.locals import *

samplerate = float(44100)                                                                                   # Hz
SampleLength = 22050                                                                                        # seconds
amplitude = 0.4
BitDepth = 65000
Soundtuple = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
noise_out = wave.open('keyboard.wav', 'w')
noise_out.setparams(Soundtuple)

values = []


def a4():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 440.000 * (i/Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def b4():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 493.883 * (i/Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.writeframes(value_str)


def c5():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 523.251 * (i/Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.writeframes(value_str)


def d5():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 587.330 * (i/Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def e5():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 659.255 * (i / Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def f5():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 698.456 * (i / Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def g5():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 783.991 * (i / Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def e6():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 1318.51 * (i / Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def b5():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 987.767 * (i / Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def c6():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 1046.50 * (i / Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def d6():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 1174.66 * (i / Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def a5():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 880.000 * (i / Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def f6():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 1396.91 * (i / Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def a6():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 1760.00 * (i / Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def g6():
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * 1567.98 * (i / Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def whitespace():
    for i in range(0, Soundtuple[3]):
        value = math.sin(0)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)
    value_str = ''.join(values)
    noise_out.writeframes(value_str)


def close_sound():
    noise_out.close()


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
            a4()

        if keys[K_s]:
            print 'E4'
            b4()

        if keys[K_d]:
            print 'C5'
            c5()

        if keys[K_f]:
            print 'D5'
            d5()

        if keys[K_g]:
            print 'E5'
            e5()

        if keys[K_h]:
            print 'F5'
            f5()

        if keys[K_j]:
            print 'G5'
            g5()

        if keys[K_k]:
            print 'A5'
            a5()

        if keys[K_l]:
            print 'B5'
            b5()

        if keys[K_z]:
            print 'C6'
            c6()

        if keys[K_x]:
            print 'D6'
            d6()

        if keys[K_c]:
            print 'E6'
            e6()

        if keys[K_v]:
            print 'F6'
            f6()

        if keys[K_b]:
            print 'G6'
            g6()

        if keys[K_SPACE]:
            print 'Silence'
            whitespace()

        if keys[K_RETURN]:
            print 'Sound Closed'
            close_sound()