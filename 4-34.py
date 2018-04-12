#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:02:49 2018

@author: rtataru
"""

"""
    a -> height
    b -> position of centre
    c -> the width of the bell
"""

import numpy as np
import matplotlib.pyplot as plt

def myGaussBell(a, b, c, t):
    res = []
    for x in t:
        val = a * np.exp((-1) * ((x - b) ** 2) / (2 * (c ** 2)))
        res.append(val)
    return res

t = np.arange(-3, 3, .05)
plt.plot(myGaussBell(3, 0, 1, t))
    