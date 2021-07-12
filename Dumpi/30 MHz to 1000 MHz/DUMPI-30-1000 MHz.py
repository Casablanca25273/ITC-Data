import pandas as pd
import pylab
import numpy as np



data1 = pd.read_csv ('/home/tankiso/Documents/2021 SARAO Graduate Programme/ITC Data/Dumpi/30 MHz to 1000 MHz/DUMPI-30to1-PWR-H.csv', sep=';', skiprows=25)
#print (data1)
data2 = pd.read_csv ('/home/tankiso/Documents/2021 SARAO Graduate Programme/ITC Data/Dumpi/30 MHz to 1000 MHz/DUMPI-30to1-PWR-LASER-H.CSV', sep=';', decimal=',', skiprows=25)
#print (data2)
data3 = pd.read_csv ('/home/tankiso/Documents/2021 SARAO Graduate Programme/ITC Data/Dumpi/30 MHz to 1000 MHz/DUMPI-30to1-PWR-LASER-V.CSV', sep=';', decimal=',', skiprows=25)
#print (data3)
data4 = pd.read_csv ('/home/tankiso/Documents/2021 SARAO Graduate Programme/ITC Data/Dumpi/30 MHz to 1000 MHz/DUMPI-30to1-PWR-V.CSV', sep=';', skiprows=25)
array = np.asarray(data1)
#print (array)
array1 = np.asarray(data2)
#print (array1)
array2 = np.asarray(data3)
#print (array2)
array3 = np.asarray(data4)
freq = array[:,0]/1000000.00  #creates evenly spaced freq sequence at the specified parameters
#print(freq)
lvl1 = array[:,1] 
#print(lvl1)
lvl2 = array1[:,1]
#print(lvl2)
lvl3 = array2[:,1]
#print(lvl3)
lvl4 = array3[:,1]
#pylab.xlim(100,1000)
pylab.plot(freq,lvl1, label = 'PWR-H')
pylab.plot(freq,lvl2, label = 'PWR-LASER-H')
pylab.plot(freq,lvl3, label = 'PWR-LASER-V')
pylab.plot(freq,lvl4, label = 'PWR-V')
#pylab.plot(freq,lvl2, label = 'Ambient', color = 'grey')
pylab.title("Total Station - 30 MHz - 1 GHz")
pylab.ylabel("Amplitude (dBuV/m)")                   #y-axis label
pylab.xlabel("Frequency (MHz)")                     #x-axis label
pylab.legend(bbox_to_anchor=(1, 0), loc='lower right', ncol=1)
pylab.grid()
pylab.savefig('Total Station - 30-1000 MHz.png')
pylab.show()
 

