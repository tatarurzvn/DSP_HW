#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:17:07 2018

@author: rtataru
"""

def pascalTraingle(row, col):
    if col == 0 or col == row:
        return 1
    else:
        return pascalTraingle(row - 1, col - 1) + pascalTraingle(row - 1, col)
    
# Test

print(pascalTraingle(5, 3))