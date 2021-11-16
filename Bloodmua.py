# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:01:18 2021

@author: Hsin-Yuan
"""
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import csv
plt.rcParams.update({"mathtext.default": "regular"})
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.dpi"] = 300
#%%
oxy_1 = pd.read_csv(r"C:\Users\User\OneDrive\桌面\IJV\blood\table and fig\fig1oxy.csv", names=['wl','mua'])
deoxy_1 = pd.read_csv(r"C:\Users\User\OneDrive\桌面\IJV\blood\table and fig\fig1deoxy.csv", names=['wl','mua'])
oxy_3 = pd.read_csv(r"C:\Users\User\OneDrive\桌面\IJV\blood\table and fig\fig4oxy.csv", names=['wl','mua'])
oxy_4 = pd.read_csv(r"C:\Users\User\OneDrive\桌面\IJV\blood\table and fig\fig5.csv", names=['wl','mua'])
oxy_5 = pd.read_csv(r"C:\Users\User\OneDrive\桌面\IJV\blood\table and fig\fig3oxy.csv", names=['wl','mua'])
deoxy_5 = pd.read_csv(r"C:\Users\User\OneDrive\桌面\IJV\blood\table and fig\fig3deoxy.csv", names=['wl','mua'])
#%%
def get_f(x):
    fblood = 0.9*(1- x/100) + 0.66*(x/100)
    return fblood

def rescaling(ori_mua, h2o_mua, x, y):  # x: original hct y:rescaled hct
    fx = get_f(x)
    fy = get_f(y)
    re_mua = (y/x)*(ori_mua- h2o_mua*fx)+ h2o_mua*fy
    return re_mua
#%%
water_ext = pd.read_csv(r"C:\Users\User\OneDrive\桌面\IJV\blood\water_mua.csv", names=['wl','ext'])
wl = water_ext['wl']
water_mua = 4*np.pi*(water_ext['ext']/wl)
f = interpolate.interp1d(wl, water_mua) 

#%%
w_mua1 = f(oxy_1['wl']/1e3)
dw_mua1 = f(deoxy_1['wl']/1e3)
low_p1= rescaling(oxy_1['mua'], w_mua1, 33.2, 41.3) #low hct of paper [1]
low_dp1= rescaling(deoxy_1['mua'], dw_mua1, 33.2, 41.3) 

high_p1= rescaling(oxy_1['mua'], w_mua1, 33.2, 52.1) #high hct of paper [1]
high_dp1= rescaling(deoxy_1['mua'], dw_mua1, 33.2, 52.1) 

w_mua3 = f(oxy_3['wl']/1e3)
low_p3 = rescaling(oxy_3['mua'], w_mua3, 42.1, 41.3) #low hct of paper [3]
high_p3 = rescaling(oxy_3["mua"], w_mua3, 42.1, 52.1) #high hct of paper [3]

w_mua4 = f(oxy_5['wl']/1e3)
dw_mua4 = f(deoxy_5['wl']/1e3)
low_p4 = rescaling(oxy_5['mua'], w_mua4, 5, 41.3) #low hct of paper [4]
low_dp4 = rescaling(deoxy_5['mua'], dw_mua4, 5, 41.3)

high_p4 = rescaling(oxy_5['mua'], w_mua4, 5, 52.1) #high hct of paper [4]
high_dp4 = rescaling(deoxy_5['mua'], dw_mua4, 5, 52.1)

w_mua5 = f(oxy_4["wl"]/1e3)
low_p5 = rescaling(oxy_4["mua"], w_mua5, 45, 41.3) #low hct of paper [5]
high_p5 = rescaling(oxy_4["mua"], w_mua5, 45, 52.1)

#%%
plt.figure(figsize=(12, 6))

plt.semilogy(oxy_1["wl"], low_p1, "r", label="Friebel et al.$^{[1]}$, oxgenated blood (Hct=41.3 %)")
plt.semilogy(oxy_1["wl"], high_p1, "r--", label="Friebel et al.$^{[1]}$, oxgenated blood (Hct=52.1 %)")
plt.semilogy(deoxy_1["wl"], low_dp1, "b", label="Friebel et al.$^{[1]}$, de-oxgenated blood (Hct=41.3 %)")
plt.semilogy(deoxy_1["wl"], high_dp1, "b--", label="Friebel et al.$^{[1]}$, de-oxgenated blood (Hct=52.1 %)")

plt.semilogy(oxy_3['wl'], low_p3, "g",label='Meinke et al.$^{[3]}$, oxgenated blood(Hct=41.3 %)')
plt.semilogy(oxy_3['wl'], high_p3, "g--",label='Meinke et al.$^{[3]}$, oxgenated blood(Hct=52.1 %)')

plt.semilogy(oxy_5['wl'], low_p4, "m", label='Roggan et al.$^{[4]}$, oxgenated blood(Hct=41.3 %)')
plt.semilogy(oxy_5['wl'], high_p4,"m--", label='Roggan et al.$^{[4]}$, oxgenated blood(Hct=52.1 %)')
plt.semilogy(deoxy_5['wl'], low_dp4, "k", label='Roggan et al.$^{[4]}$, de-oxgenated blood(Hct=41.3 %)')
plt.semilogy(deoxy_5['wl'], high_dp4,"k--", label='Roggan et al.$^{[4]}$, de-oxgenated blood(Hct=52.1 %)')


plt.plot(oxy_4['wl'], low_p5, "c", label='Yaroslavsky et al.$^{[5]}$, oxgenated blood(Hct=41.3 %)')
plt.plot(oxy_4['wl'], high_p5, "c--", label='Yaroslavsky et al.$^{[5]}$, oxgenated blood(Hct=52.1 %)')

plt.title('Blood Absorption coefﬁcient', fontsize=20)
plt.xlabel('wavelength(nm)', fontsize=16)
plt.ylabel('$\mu_a$(mm$^-1$)', fontsize=16)
plt.legend(fontsize=10)
plt.savefig("C:/Users/User/OneDrive/桌面/IJV/光學參數/blood/mua_new/figure")

#%%save data
name_list = ["Friebel et al, oxgenated blood (Hct=41.3 %)",
             "Friebel et al, oxgenated blood (Hct=52.1 %)",
             "Friebel et al, de-oxgenated blood (Hct=41.3 %)",
             "Friebel et al, de-oxgenated blood (Hct=52.1 %)",
             "Meinke et al, oxgenated blood (Hct=41.3 %)",
             "Meinke et al, oxgenated blood(Hct=52.1 %)",
             "Roggan et al, oxgenated blood(Hct=41.3 %)",
             "Roggan et al, oxgenated blood(Hct=52.1 %)",
             "Roggan et al, de-oxgenated blood(Hct=41.3 %)",
             "Roggan et al, de-oxgenated blood(Hct=52.1 %)",
             "Yaroslavsky et al, oxgenated blood(Hct=41.3 %)",
             "Yaroslavsky et al, oxgenated blood(Hct=52.1 %)"
             ]

data_list = [low_p1, high_p1, low_dp1, high_dp1, low_p3, high_p3,
             low_p4, high_p4, low_dp4, high_dp4, low_p5, high_p5
             ]

wl_list = [oxy_1["wl"], oxy_1["wl"], deoxy_1["wl"], deoxy_1["wl"],
           oxy_3['wl'], oxy_3['wl'], oxy_5['wl'], oxy_5['wl'],
           deoxy_5['wl'], deoxy_5['wl'], oxy_4['wl'], oxy_4['wl']
           ]

for name, data ,wl in zip(name_list, data_list, wl_list) :
    with open("C:/Users/User/OneDrive/桌面/IJV/光學參數/blood/mua_new/" + name + ".csv" , 'w', newline='') as csvfile:
    
      writer = csv.writer(csvfile)
      # 寫入一列資料
      writer.writerow(['wavelength', 'mua'])
      # print(name, data, wl)
      # 寫入另外幾列資料
      for i in range(len(data)):
          writer.writerow([wl[i], data[i]])

#%%
files = glob.glob(r"C:\Users\User\OneDrive\桌面\IJV\光學參數\blood\mua_new\*.csv")

df = pd.concat((pd.read_csv(file) for file in files), ignore_index=True)


wl_filter = (df["wavelength"] >725) & (df["wavelength"] <875)

wl = df["wavelength"][wl_filter]







