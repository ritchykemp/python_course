from math import *
import numpy as np 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.stats as sst
from scipy.optimize import curve_fit

def fit(x,a,b,c):
    return a*x**2+b*x+c

Data= []
i = 0
fobj = open("session5/Weatherstations.txt", "r")
for element in fobj:
    
    element= element.strip()
    splitline = element.split("\t")
    #print (splitline)
    if i > 0:
        Altitude = float(splitline[0])
        Temp = float(splitline[1])
        Data.append([Altitude,Temp])
    i+=1
fobj.close()

Array = np.array(Data)

numBins = 100
stats = sst.binned_statistic(Array[:,0], Array[:,1], statistic='mean', bins=numBins, range=None)
stats_altitude = stats[1][0:numBins] #get centre of bin
stats_temp = (stats[0]) #get mean of all samples in bin

popt,pcov=curve_fit(fit,Array[:,0],Array[:,1])

residuals = Array[:,1] - fit(Array[:,0], *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((Array[:,1]-np.mean(Array[:,1]))**2)
r_squared = 1 - (ss_res / ss_tot)
print("R_Squared fit :", r_squared)

xLine = np.linspace(min(Array[:,0]), max(Array[:,0]), num=1000)
yLine = fit(xLine,*popt)

plt.plot(Array[:,0], Array[:,1],'r.') #'r." steht für Roter punkt ploten
plt.plot(xLine, yLine, 'b-')
plt.title("Höhe vs. Temperatur",fontsize=12)
plt.ylabel('Temperatur in °C')
plt.xlabel('height in m')
plt.savefig("session5/Weatherstation.png",dpi=300)
plt.close()
