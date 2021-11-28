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
large_data = glob.glob(r"D:\IJV\test_bc_eric_largeijv_mus_lb\output\mcx_output\*.jdat") #管徑大
small_data = glob.glob(r"D:\IJV\test_bc_eric_smallijv_mus_lb\output\mcx_output\*.jdat") #管徑小

with open(r"D:\IJV\test_bc_eric_largeijv_mus_lb\config.json") as L:
    large_config = json.load(L)
with open(r"D:\IJV\test_bc_eric_smallijv_mus_lb\config.json") as S:
    small_config = json.load(S)

#%% get mean path length & reflentance 
mua = np.array([0.1,   # skin
                0.1,   # fat
                0.05,  # muscle
                0.3,   # IJV
                0.3    # CCA
                ])
largemeanpath = postprocess.getMeanPathlength(1.51, 1.51, 0.22, 18, large_data, mua) 
smallmeanpath = postprocess.getMeanPathlength(1.51, 1.51, 0.22, 18, small_data, mua)    
largeref = postprocess.getReflectance(1.51, 1.51, 0.22, 18, large_data, large_config["PhotonNum"], mua)    
smallref = postprocess.getReflectance(1.51, 1.51, 0.22, 18, small_data, small_config["PhotonNum"], mua)
#%% get other mean path length & reflentance
muap = np.array([0.1,  # skin
                0.1,   # fat
                0.05,  # muscle
                0.2,   # IJV
                0.3    # CCA
                ])
largerefp = postprocess.getReflectance(1.51, 1.51, 0.22, 18, large_data, large_config["PhotonNum"], muap)
smallrefp = postprocess.getReflectance(1.51, 1.51, 0.22, 18, small_data, small_config["PhotonNum"], muap)
largemeanpathp = postprocess.getMeanPathlength(1.51, 1.51, 0.22, 18, large_data, muap)
smallmeanpathp = postprocess.getMeanPathlength(1.51, 1.51, 0.22, 18, small_data, muap)
#%%  
largePathArr = largemeanpath.reshape(-1, 3, 3, 2).mean(axis=-1)
largeRefArr = largeref.reshape(-1, 3, 3, 2).mean(axis=-1)
smallPathArr = smallmeanpath.reshape(-1, 3 ,3, 2).mean(axis=-1)
smallRefArr = smallref.reshape(-1, 3, 3, 2).mean(axis=-1)
#%%
largeRefpArr = largerefp.reshape(-1, 3, 3, 2).mean(axis=-1)
smallPathpArr = smallmeanpathp.reshape(-1, 3 ,3, 2).mean(axis=-1)
smallRefpArr = smallrefp.reshape(-1, 3, 3, 2).mean(axis=-1)
largePathpArr = largemeanpathp.reshape(-1, 3, 3, 2).mean(axis=-1)

#%%
Imax = smallRefArr.mean(axis=1).mean(axis=0)
Imin = largeRefArr.mean(axis=1).mean(axis=0)
L = largePathArr.mean(axis=1).mean(axis=0)- smallPathArr.mean(axis=1).mean(axis=0)
Ipmax = smallRefpArr.mean(axis=1).mean(axis=0)
Ipmin = largeRefpArr.mean(axis=1).mean(axis=0)
Lp = largePathpArr.mean(axis=1).mean(axis=0)- smallPathpArr.mean(axis=1).mean(axis=0)
#%%
real = np.log(Ipmin/Ipmax)- np.log(Imin/Imax)
cal = (((mua[-2])*L)-((muap[-2])*Lp)+ (mua[-3])*(Lp-L))

print(real) ; print(cal)


#%%
largepathcv = ((largePathArr.mean(axis=1)).std(axis=0)/(largePathArr.mean(axis=1)).mean(axis=0))/np.sqrt(79)
smallpathcv = ((smallPathArr.mean(axis=1)).std(axis=0)/(smallPathArr.mean(axis=1)).mean(axis=0))/np.sqrt(148)
largerefcv = ((largeRefArr.mean(axis=1)).std(axis=0)/(largeRefArr.mean(axis=1)).mean(axis=0))/np.sqrt(79)
smallrefcv = ((smallRefArr.mean(axis=1)).std(axis=0)/(smallRefArr.mean(axis=1)).mean(axis=0))/np.sqrt(148)
print(largepathcv); print(smallpathcv)
print(largerefcv); print(smallrefcv)

largepathpcv = ((largePathpArr.mean(axis=1)).std(axis=0)/(largePathpArr.mean(axis=1)).mean(axis=0))/np.sqrt(79)
smallpathpcv = ((smallPathpArr.mean(axis=1)).std(axis=0)/(smallPathpArr.mean(axis=1)).mean(axis=0))/np.sqrt(148)
largerefpcv = ((largeRefpArr.mean(axis=1)).std(axis=0)/(largeRefpArr.mean(axis=1)).mean(axis=0))/np.sqrt(79)
smallrefpcv = ((smallRefpArr.mean(axis=1)).std(axis=0)/(smallRefpArr.mean(axis=1)).mean(axis=0))/np.sqrt(148)
print(largepathpcv); print(smallpathpcv)
print(largerefpcv); print(smallrefpcv)


#%%
mus = 119.7 ; musp = 119.7









