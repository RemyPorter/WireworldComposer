"""Wireworld Simulator, with Hooks for Sinking Output"""

import numpy as np

H = 1
T = 2
C = 3
E = 0

def normalize(size, coord):
    """Turns the coordinate system into a toroid"""
    x,y = coord
    return np.array([x % size, y % size])

