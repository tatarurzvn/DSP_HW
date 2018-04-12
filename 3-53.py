#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 21:49:59 2018

@author: tatarurzvn
"""
import numpy as np
import matplotlib.pyplot as plt

def myRampPulse(A, t1, t2, t):
    res = []
    for x in t:
        if (t1 <= x) and (x <= t2):
            val = (A / (t2 - t1)) * (x - t1)
            res.append(val)
        else:
            res.append(0)
    return res

# Test
A = 1
t1, t2 = 3, 4
t = np.arange(0, 5, .05)
plt.plot(myRampPulse(A, t1, t2, t))

def myStairs(t):
    res = []
    for x in t:
        res.append(np.floor(x))
    return res

# Test
t = np.arange(0, 5, .05)
plt.plot(myStairs(t))

def mySawtooth(t):
    res = []
    for x in t:
        res.append(x - np.floor(x))
    return res

# Test
t = np.arange(0, 5, .05)
plt.plot(mySawtooth(t))

