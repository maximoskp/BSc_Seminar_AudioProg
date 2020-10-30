# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:36:52 2020

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt


'''
sr = 44100
duration = 1
t = np.arange(duration*sr)/sr

f = 200

s = np.sin( 2*np.pi*f*t )

idx = np.ceil(44100/f).astype(int)

plt.plot( t[:idx] , s[:idx] )
'''

'''
# QUANTIZATION
sr = 44100
duration = 1
t = np.arange(duration*sr)/sr

f = 1

s = np.sin( 2*np.pi*f*t )
q = np.interp(s, (-1, 1), (0,256))
p = np.floor( q )
p[ p >= 256 ] = 255

s_quantised = np.interp( p,(0,255), (-1,1) )

q_noise = s - s_quantised;

plt.plot( t , s )
plt.plot( t , s_quantised )
plt.plot( t , q_noise )
'''

sr = 44100
duration = 0.05
t = np.arange(duration*sr)/sr

f = 1

s = np.sin( 2*np.pi*f*t )
plt.plot( t , s )

