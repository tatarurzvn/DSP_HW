#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 20:52:07 2018

@author: tatarurzvn
"""

"""
Define an array w/ 100 elements,
where xn+1 = sqrt(xn + 1), x1 = 100
"""
import numpy as np

x = [100]

for i in range(1, 100):
    x.append(np.sqrt(x[i - 1] + 1))
    
print(x)