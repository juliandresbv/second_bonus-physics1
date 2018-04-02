"""
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging

#from second_bonus_physics1 import __version__

__author__ = "Julian Bermudez"
__copyright__ = "Julian Bermudez"
__license__ = "mit"

_logger = logging.getLogger(__name__)
"""

import numpy as np
import matplotlib.pyplot as plt

"""

"""
#x = np.arange(-100, 100, 0.1)

"""
Function which defines the combination of Elastic Potencial Energy (Up_e.) and Gravitational Potencial Energy (Up_g)
"""
def f(x, k, m):
    return ((1/2)*(k)*(x**2) + (m)*(9.8)*(x)).astype(np.float)

def set_k_m():
    raw_k = input("Input the value for k (spring constant): ")
    if raw_k is None:
        raw_k = 1

    raw_m = input("Input the value for m (mass of the particle/body): ")
    if raw_m is None:
        raw_m = 1

    float_k = float(raw_k)
    float_m = float(raw_m)

#plt.plot(x, f(x, 0, 0))
#plt.show()

if __name__ == "main":
    set_k_m()