#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:14:21 2018

@author: rtataru
"""

"""
Solve the system {x1 + 2x2 = 5,
                    3x1 + 4x2 = 11}
"""

import numpy as np

A = np.array([[1, 2],
               [3, 4]])

b = np.array([5, 11])

x = np.linalg.solve(A, b)

print(x)
