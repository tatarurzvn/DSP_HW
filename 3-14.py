#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:24:27 2018

@author: rtataru
"""

import matplotlib.pyplot as plt
import numpy as np

def mySine(A, freq, phi, t):
    return A * np.sin(2 * np.pi * freq * t + phi)

# Test
# t = np.arange(-5, 5, .05)
# plt.plot(mySine(2, .5, 0, t) + 2)

t = np.arange(0, 10, .01)
q = mySine(10, 2, 0, t)

f = open("3-14.txt", "w+")

for x in q:
    f.write("%f\n" % x)

f.close()