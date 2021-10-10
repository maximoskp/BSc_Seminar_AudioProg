#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:47:27 2020

@author: max
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

sr = 1000

t = np.arange( sr )/sr

f = 700

s = np.sin( 2*np.pi*f*t )

plt.plot( t , s )

sd.play( s , sr )
