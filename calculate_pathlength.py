#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:17:59 2022

@author: md703
"""

import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import postprocess
import jdata as jd
import json
#%%
muaPath = "mua.json"
with open(os.path.join("small_ijv", muaPath)) as f:
    mua = json.load(f)
muaUsed =[mua["1: Air"],
          mua["2: PLA"],
          mua["3: Prism"],
          mua["4: Skin"],
          mua["5: Fat"],
          mua["6: Muscle"],
          mua["7: Muscle or IJV (Perturbed Region)"],
          mua["8: IJV"],
          mua["9: CCA"]
          ]

#%%
ls = glob.glob("small_*")

#%%
muaSkin = np.linspace(0.0006, 0.2458, 5)
muaFat = np.linspace(0.02622, 0.1224, 5)
muaMuscle = np.linspace(0.0046, 0.054, 5)
muaIJV = np.linspace(0.2622, 0.7245, 5)

muaSet = np.zeros([len(muaSkin)*len(muaFat)*len(muaMuscle)*len(muaIJV)])
PathlengthSet = np.empty([len(muaSet), 19])

index = 0
for sessionId in ls[:1]:
    for skin in muaSkin:
        muaUsed[3] = skin       
        for fat in muaFat:
           muaUsed[4] = fat            
           for muscle in muaMuscle:
               muaUsed[5] = muscle               
               for index, mu in enumerate(muaIJV):
                    muaUsed[-2] = mu
                    # muaUsed[-3] = mu
                    muaSet[index] = muaUsed[-2]
                    PathlengthSet[index] = (postprocess.getMeanPathlength(sessionId, muaUsed)[1].mean(axis=0)[:, -3])
                    index += 1
                
    np.save(f"/home/md703/Desktop/pathlength/{sessionId}", PathlengthSet)
    
np.save("/home/md703/Desktop/pathlength/muaSet", muaSet)











