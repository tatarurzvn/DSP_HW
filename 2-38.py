# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np

t=np.arange(-5., 5., 0.1)
a=t**2-t+1
plt.subplot(2, 1, 1)
plt.plot(t, a, '*')
plt.subplot(2, 1, 2)