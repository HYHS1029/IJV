# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:28:12 2022

@author: Hsin-Yuan
"""
import numpy as np
import torch
import torch.nn as nn
import torch.autograd as Variable
import pandas as pd
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt
#%%
large_ijv_730 = np.load(r"D:\IJV\reflectance\large_ijv_730.npy")[:,7]
large_ijv_760 = np.load(r"D:\IJV\reflectance\large_ijv_760.npy")[:,7]
large_ijv_810 = np.load(r"D:\IJV\reflectance\large_ijv_810.npy")
large_ijv_850 = np.load(r"D:\IJV\reflectance\large_ijv_850.npy")
small_ijv_730 = np.load(r"D:\IJV\reflectance\small_ijv_730.npy")[:,7]
small_ijv_760 = np.load(r"D:\IJV\reflectance\small_ijv_760.npy")[:,7]
small_ijv_810 = np.load(r"D:\IJV\reflectance\small_ijv_810.npy")
small_ijv_850 = np.load(r"D:\IJV\reflectance\small_ijv_850.npy")
#%%
mua_set_730 = np.load(r"D:\IJV\reflectance\muaSet_730.npy")[:, -2]
mua_set_760 = np.load(r"D:\IJV\reflectance\muaSet_760.npy")[:, -2]
mua_set_810 = np.load(r"D:\IJV\reflectance\muaSet_810.npy")[:, -2]
mua_set_850 = np.load(r"D:\IJV\reflectance\muaSet_850.npy")[:, -2]

#%%
def SO2(mua, wl):
    if wl == 730:    
        x1 = 39/64532
        x2 = 110.22/64500
        so2 = (mua/(150) - x2)*(1/(x1 - x2))
    if wl == 760:    
        x1 = 586/64532
        x2 = 15485.2/64500
        so2 = (mua/150 - x2)*(1/(x1 - x2))
    if wl == 810:    
        x1 = 8640/64532
        x2 = 7170.8/64500
        so2 = (mua/150 - x2)*(1/(x1 - x2))
    if wl == 850:    
        x1 = 10580/64532
        x2 = 6913.2/64500
        so2 = (mua/150 - x2)*(1/(x1 - x2))
    return so2

# oxygen_saturation = SO2(mua_set_730, 730)

#%%
    




