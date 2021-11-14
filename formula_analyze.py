# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:54:03 2021

@author: Hsin-Yuan
"""
import glob
import numpy as np
import matplotlib.pyplot as plt
import postprocess
import jdata as jd
import json
#%%read data
large_data = glob.glob(r"D:\IJV\test_bc_eric_largeijv_mus_lb\output\mcx_output\*.jdat")
small_data = glob.glob(r"D:\IJV\test_bc_eric_smallijv_mus_lb\output\mcx_output\*.jdat")

with open(r"D:\IJV\test_bc_eric_largeijv_mus_lb\config.json") as L:
    large_config = json.load(L)
with open(r"D:\IJV\test_bc_eric_smallijv_mus_lb\config.json") as S:
    small_config = json.load(S)

#%% get mean path length & reflentance
largemeanpath = postprocess.getMeanPathlength(1.51, 1.51, 0.22, 18, large_data)
smallmeanpath = postprocess.getMeanPathlength(1.51, 1.51, 0.22, 18, small_data)    
largeref = postprocess.getReflectance(1.51, 1.51, 0.22, 18, large_data, large_config["PhotonNum"])    
smallref = postprocess.getReflectance(1.51, 1.51, 0.22, 18, small_data, small_config["PhotonNum"])
#%% get other mean path length & reflentance
largerefp = postprocess.getReflectance(1.51, 1.51, 0.22, 18, large_data, large_config["PhotonNum"])
smallrefp = postprocess.getReflectance(1.51, 1.51, 0.22, 18, small_data, small_config["PhotonNum"])
largemeanpathp = postprocess.getMeanPathlength(1.51, 1.51, 0.22, 18, large_data)
smallmeanpathp = postprocess.getMeanPathlength(1.51, 1.51, 0.22, 18, small_data)
#%%  
largePathArr = largemeanpath.reshape(-1, 3, 3, 2).mean(axis=-1)
largeRefArr = largeref.reshape(-1, 3, 3, 2).mean(axis=-1)
smallPathArr = smallmeanpath.reshape(-1, 3 ,3, 2).mean(axis=-1)
smallRefArr = smallref.reshape(-1, 3, 3, 2).mean(axis=-1)
#%%
largePathpArr = largemeanpathp.reshape(-1, 3, 3, 2).mean(axis=-1)
largeRefpArr = largerefp.reshape(-1, 3, 3, 2).mean(axis=-1)
smallPathpArr = smallmeanpathp.reshape(-1, 3 ,3, 2).mean(axis=-1)
smallRefpArr = smallrefp.reshape(-1, 3, 3, 2).mean(axis=-1)

#%%
Imax = smallRefArr.mean(axis=0)
Imin = largeRefArr.mean(axis=0)
L = largePathArr.mean(axis=0)-smallPathArr.mean(axis=0)

#%%
















