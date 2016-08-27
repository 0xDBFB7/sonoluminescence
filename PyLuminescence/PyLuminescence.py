from __future__ import division
import math
import pyaudio as PyAudio # sudo apt-get install python-pyaudio
from time import sleep
import sys
import audioop
import struct
from array import array
import pygame
import Tkinter
from Tkinter import *
import json
from pygame.locals import *
from pygame.mixer import Sound, get_init, pre_init

#config = open("PyLuminescence.config",'r+')
global best_frequency
global frequency_range
frequency_range = [21000,25000]
class Note(Sound):

    def __init__(self, frequency, volume=.1):
        self.frequency = frequency
        Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in xrange(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples
p = PyAudio.PyAudio()
stream = p.open(format=PyAudio.paInt16, # 8bit
                    channels=1, # mono
                    rate=96000,
                    input=True,
                    output=False,
                    frames_per_buffer=2048)
pre_init(96000, -16, 1, 1024)
pygame.init()

top = Tkinter.Tk()
top.title("PyLuminescence")


def Tune():
    volume = 0.4
    temp_best_amplitude=0.0
    temp_best_frequency=0.0
    for frequency in range(21000,25000,10):
        Note(frequency,volume).play(-1)
        sleep(0.1)
        stream.start_stream()
        data=stream.read(2048)
        stream.stop_stream()
        amplitude = audioop.maxpp(data,2)
        Note(frequency).stop()
        w.create_rectangle(int(((frequency-frequency_range[0])/float(frequency_range[1]-frequency_range[0]))*500.0), 50, int(((frequency-frequency_range[0])/float(frequency_range[1]-frequency_range[0]))*500.0)+1, 50-((amplitude/65536.0)*50), fill="blue")
        w.update()
        #w.delete("all")
        if(amplitude > temp_best_amplitude):
            temp_best_amplitude=amplitude
            temp_best_frequency=frequency
            display_amplitude.configure(text=("Best Amplitude: "+ str(amplitude)))
            display_amplitude.configure(text=("Best Frequency: "+ str(frequency)))
B = Tkinter.Button(top, text ="Tune", command = Tune)
B.grid(row=0,column=1)
display_amplitude = Label(top, text="") # we need this Label as a variable!
display_amplitude.grid(row=1,column=1)
display_amplitude.configure(text="Amplitude: 0")


display_frequency = Label(top, text="") # we need this Label as a variable!
display_frequency.grid(row=2,column=1)
display_frequency.configure(text="Frequency: 0")

w = Canvas(top, width=500, height=50)
w.grid(row=3,column=1)

top.mainloop()
