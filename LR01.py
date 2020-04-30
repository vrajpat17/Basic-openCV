# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:42:03 2020

@author: VRAJ PATEL
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
#matplotlib inline


dataset = pd.read_csv('/Users/VRAJ PATEL/Desktop/Ready/Weather.csv', low_memory=False)

dataset.describe()
