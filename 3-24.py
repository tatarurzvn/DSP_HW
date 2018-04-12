#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 21:32:07 2018

@author: tatarurzvn
"""
import numpy as np
import matplotlib.pyplot as plt

def myRectangularPulse(A, t1, t2, t):
    res = []
    for x in t:
        if (t1 <= x) and (x <= t2):
            res.append(A)
        else:
            res.append(0)
    return res

A = 2
t1 = 1
t2 = 2
t = np.arange(-1, 5, .1)
plt.plot(myRectangularPulse(A, t1, t2, t))