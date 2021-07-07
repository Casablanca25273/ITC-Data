# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 09:25:46 2021

@author: tankiso
"""

import pandas as pd
import pylab
import numpy as np
import matplotlib.pyplot as plt


data1 = pd.read_excel (r'/home/tankiso/Documents/2021 SARAO Graduate Programme/ITC Data/Total Station_100-1 RD.xlsx', skiprows=3)
#print (data1)
array = np.asarray(data1)
#print (array)
freq = array[:,0]/1000000.00  #creates evenly spaced freq sequence at the specified parameters
#print(freq)
lvl1 = array[:,1] 
#print(lvl1)
lvl2 = array[:,2]
#print (lvl2)
lvl3 = array[:,3]
#print (lvl3)
pylab.xlim(100,1000)
pylab.plot(freq,lvl1, label = 'Idle')
pylab.plot(freq,lvl2, label = 'Ambient', color = 'grey')
pylab.title("Linertec (Idle) - 100 MHz - 1 GHz")
pylab.ylabel("Amplitude (dBuV/m)")                   #y-axis label
pylab.xlabel("Frequency (MHz)")                     #x-axis label
pylab.legend(bbox_to_anchor=(1, 0), loc='lower right', ncol=1)
pylab.grid()
pylab.savefig('Idle and Ambient plot.png')
pylab.show()
 
lvl_diff = np.subtract(lvl1,lvl2,)                   #calculating the difference between the two plots
pylab.plot(freq,lvl_diff, label = 'Difference-Idle-Ambient')                           #plotting the difference plot
pylab.title("Linertec (Idle) - 100 MHz - 1 GHz Delta")
pylab.xlabel("Frequency (MHz)")
pylab.ylabel("Amplitude (dBuV/m)")
pylab.axvspan(100, 200, color='green', alpha=0.5)
pylab.text(155, 18, 'HERA', fontsize=15, color='blue', rotation=90)
pylab.axvspan(580, 1000, color='pink', alpha=0.5)
pylab.text(750, 13, 'UHF', fontsize=15, color='blue', rotation=90)
pylab.axvspan(900, 1000,   ymin = 0.02, ymax = 0.87, color='cyan', alpha=0.5)
pylab.text(950, 15, 'L-BAND', fontsize=15, color='blue', rotation=90)
pylab.xlim(100,1000)
pylab.legend()
pylab.grid()
pylab.savefig('Difference Idle and Ambient plot.png')
pylab.show()

pylab.plot(freq,lvl3, label = 'Measure')
pylab.plot(freq,lvl2, label = 'Ambient', color = 'grey')
pylab.title("Linertec (Measure) - 100 MHz - 1 GHz")
pylab.ylabel("Amplitude (dBuV/m)")                   #y-axis label
pylab.xlabel("Frequency (MHz)")                     #x-axis label
pylab.legend(bbox_to_anchor=(1, 0), loc='lower right', ncol=1)
pylab.xlim(100,1000)
pylab.grid()
pylab.savefig('Measure and Ambient plot.png')
pylab.show()

lvl_diff = np.subtract(lvl3,lvl2)                   #calculating the difference between the two plots
pylab.plot(freq,lvl_diff, label = 'Difference-Measure-Ambient')                           #plotting the difference plot
pylab.title("Linertec (Measure) - 100 MHz - 1 GHz Delta")
pylab.xlabel("Frequency (MHz)")
pylab.ylabel("Amplitude (dBuV/m)")
pylab.axvspan(100, 200, color='green', alpha=0.5)
pylab.text(155, 45, 'HERA', fontsize=15, color='blue', rotation=90)
pylab.axvspan(580, 1000, color='pink', alpha=0.5)
pylab.text(750, 45, 'UHF', fontsize=15, color='blue', rotation=90)
pylab.axvspan(900, 1000, ymin = 0.017, ymax = 0.87, color='cyan', alpha=0.5)
pylab.text(950, 45, 'L-BAND', fontsize=15, color='blue', rotation=90)
pylab.xlim(100,1000)
pylab.legend()
pylab.grid()
pylab.savefig('Difference Measure and Ambient plot.png')
pylab.show()


data1 = pd.read_excel (r'/home/tankiso/Documents/2021 SARAO Graduate Programme/ITC Data/Total Station_1-3 RD.xlsx', skiprows=3)
#print (data1)
array = np.asarray(data1)
freq = array[:,0]  #creates evenly spaced freq sequence at the specified parameters
plt.xlim([1000000000, 3000000000])
#print(freq)
lvl4 = array[:,1]
lvl5 = array[:,2]
pylab.plot(freq,lvl4, label = 'Idle')
pylab.plot(freq,lvl5, label = 'Ambient', color = 'grey')
pylab.title("Linertec (Idle) - 1 GHz - 3 GHz")
pylab.ylabel("Amplitude (dBuV/m)")                   #y-axis label
pylab.xlabel("Frequency (GHz)")                     #x-axis label
pylab.legend(bbox_to_anchor=(1, 0), loc='lower right', ncol=1)
pylab.grid()
pylab.savefig('Idle and Ambient plot 1-3 GHz.png')
pylab.show()


lvl_diff = np.subtract(lvl4,lvl5)                   #calculating the difference between the two plots
pylab.plot(freq,lvl_diff, label = 'Difference-Idle-Ambient')                           #plotting the difference plot
pylab.title("Linertec (Idle) - 1 GHz - 3 GHz Delta")
pylab.xlabel("Frequency (GHz)")
pylab.ylabel("Amplitude (dBuV/m)")
pylab.axvspan(1000000000, 1015000000, color='pink', alpha=0.5)
pylab.text(1009000000, -5.5, 'UHF', fontsize=4, color='blue', rotation=90)
pylab.text(1009000000, 5.8, 'UHF', fontsize=4, color='blue', rotation=90)
pylab.axvspan(1000000000, 1670000000, ymin = 0.08, ymax = 0.95, color='cyan', alpha=0.5)
pylab.text(1250000000, 4.7, 'L-BAND', fontsize=15, color='blue')
pylab.axvspan(1750000000, 3000000000, ymin = 0, ymax = 1, color='grey', alpha=0.5)
pylab.text(2250000000, 5, 'S-BAND', fontsize=15, color='blue')
pylab.xlim(1000000000,3000000000)
pylab.legend(bbox_to_anchor=(1, 0), loc='lower right', ncol=1)
pylab.grid()
pylab.savefig('Difference Idle and Ambient plot 1-3 GHz.png')
pylab.show()