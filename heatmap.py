# -*- coding: utf-8 -*-

"""

Created on Thu Jul 22 11:09:09 2021

 

@author: Lotzkar

"""

 

#%% Importing packages

 

import numpy as np #numpy package for stat functions

 

import pandas as pd #pandas package for scraping

pd.__version__

 

#pd is the common "alias" used in Python community

#http://pandas.pydata.org/pandas-docs/stable/

 

#df is the name for DataFrame used here

 

import matplotlib.pyplot as plt #package for plotting and visualizing data

 

import matplotlib.patches as mpatches #for matplot legend

 

from statsmodels.tsa.stattools import coint #for cointegration testing

 

from scipy.stats import shapiro #shapiro-wilk test for normality

 

import seaborn #for cointegration heatmap

 

import os

 

#%%