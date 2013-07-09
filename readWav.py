#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wave
import pylab
import numpy

# open the wave file
file = wave.open(r"/home/sniper/Dropbox/5s20db.wav", "rb")

params = file.getparams();
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = file.readframes(nframes)
file.close()

wave_data = numpy.fromstring(str_data, dtype = numpy.short)
wave_data.shape = -1, 2
wave_data = wave_data.T 
time = numpy.arange(0, nframes) * (1.0 / framerate)

# draw 
pylab.subplot(211)
pylab.plot(time, wave_data[0])
pylab.subplot(212)
pylab.plot(time, wave_data[1], c = "g")
pylab.xlabel("time (seconds)")
pylab.show()
