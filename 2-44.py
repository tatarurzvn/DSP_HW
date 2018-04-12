#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 20:58:47 2018

@author: tatarurzvn
"""

"""
Compare the execution times for solving a linear system
of degree 1000 using x = A/b and x = inv(A) * b
"""

import numpy as np
import time

A = np.random.rand(1000, 1000)
b = np.random.rand(1000)

t0 = time.time()
x = np.linalg.solve(A, b)
t1 = time.time()
print(t1 - t0)

t0 = time.time()
x = np.linalg.inv(A) * b
t1 = time.time()
print(t1 - t0)