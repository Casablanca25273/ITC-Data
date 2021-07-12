import pandas as pd
import pylab
import numpy as np



data1 = pd.read_csv ('/home/tankiso/Documents/2021 SARAO Graduate Programme/ITC Data/Dumpi/1-6 GHz/DUMPI-1to6-PWR-H.CSV', sep=';', decimal=',', skiprows=36)
#print (data1)
data2 = pd.read_csv ('/home/tankiso/Documents/2021 SARAO Graduate Programme/ITC Data/Dumpi/1-6 GHz/DUMPI-1to6-PWR-LASR-H.CSV', sep=';', decimal=',', skiprows=36)
#print (data2)
data3 = pd.read_csv ('/home/tankiso/Documents/2021 SARAO Graduate Programme/ITC Data/Dumpi/1-6 GHz/DUMPI-1to6-PWR-LASR-V.CSV', sep=';', decimal=',', skiprows=36)
#print (data3)
data4 = pd.read_csv ('/home/tankiso/Documents/2021 SARAO Graduate Programme/ITC Data/Dumpi/1-6 GHz/DUMPI-1to6-PWR-V.CSV', sep=';', decimal=',', skiprows=36)
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
pylab.plot(freq,lvl1, label = 'PWR-H')
pylab.plot(freq,lvl2, label = 'PWR-LASER-H')
pylab.plot(freq,lvl3, label = 'PWR-LASER-V')
pylab.plot(freq,lvl4, label = 'PWR-V')
pylab.title("Total Station - 1 GHz - 6 GHz")
pylab.ylabel("Amplitude (dBuV/m)")                   #y-axis label
pylab.xlabel("Frequency (MHz)")                     #x-axis label
pylab.legend(bbox_to_anchor=(1, 0), loc='lower right', ncol=1)
pylab.grid()
pylab.savefig('Total Station - 1-6 GHz.png')
pylab.show()
 

