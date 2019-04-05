#!/usr/bin/env python3
"""
Script Doc String
"""
#import system libraries
import os,sys
#import processing libraries
import numpy as np
from numpy.fft import fft,ifft,fftfreq
import pandas as pd
#import visualization libraries
import matplotlib.pyplot as plt

def create_magsynth():
    """
    Function Doc String
    """
    pass #put outline of code here

def create_magsource():
    """
    Make magnetic source
    """
    pass

def apply_earthfilter():
    """
    Make earth filter
    """
    pass

def read_gradstien(file_path):
    """
    Read Gradstien et al. 2012 timescale from data file
    """
    pass

if __name__=="__main__":
    if "-h" in sys.argv:
        help(__name__)

