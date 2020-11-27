# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:08:28 2020

@author: user
"""

import librosa
import audio_utils as au
import soundfile as sf
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

filename = 'audio_files/celloSampleStereo.wav'

y, sr = librosa.load(filename)

p = au.get_stereo_random_part( y , s=0 , e=20000 , d_min=1000 , d_max=2000 , pan=0.1 )

sf.write('audio_files/result.wav', p, 44100, 'PCM_24')

sd.play(p, sr)

plt.subplot(211)
plt.plot( np.arange( p.shape[0] ) , p[:,0] )
axes = plt.gca()
axes.set_ylim([-1,1])
plt.subplot(212)
plt.plot( np.arange( p.shape[0] ) , p[:,1] )
axes = plt.gca()
axes.set_ylim([-1,1])

# example: random composition
# initialise composition of 10 secs
composition_duration = 10
sr = 44100
composition_samples = composition_duration*sr
c = np.zeros( ( composition_samples , 2 ) )
# let's place a number of notes randomly
n = 5000
for i in range( n ):
    # random note
    f = np.random.randint(50, 5000)
    a = np.random.random()
    tmp_adsr = au.make_adsr( dur_secs = np.random.random() + 0.5 )
    r = au.make_sine_with_adsr(freq=f, amp=a, adsr=tmp_adsr)
    # place note randomly within the composition
    tmp_idx = np.random.randint(composition_samples - 44100-22050)
    # apply random panning
    tmp_pan = np.random.random()
    c[ tmp_idx:(tmp_idx+r.size) , 0 ] += tmp_pan*r
    c[ tmp_idx:(tmp_idx+r.size) , 1 ] += (1-tmp_pan)*r

# normalize
c = c / np.max( np.abs( c ) )
sf.write('audio_files/random_composition.wav', c, 44100, 'PCM_24')