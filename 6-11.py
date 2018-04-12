#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:27:54 2018

@author: rtataru
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

fs = 10000
fCut1 = 2000
fCut2 = 3000
fCut3 = 4000
df = 50;

w = np.array([0, fCut1 - df, fCut1 + df, fCut2 - df, fCut2 + df, fCut3 - df, fCut3 + df, fs / 2])
w /= (fs / 2)
A = np.array([0, 0, 0, 1, 1, 0, 0, 0])
n = 50
a = 1

b = sp.signal.firls(n, w, A)