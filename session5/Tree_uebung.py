from math import *
import numpy as np 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.stats as sst
from scipy.optimize import curve_fit

def linefit(x,a,c):
    return a*x+c

def fit2(x,a,b,c):
    return a*x**2+b*x+c

def fit3(x,a,b,c,d): #übung3
    return a*x**3+b*x**2+c*x+d



Data= []

fobj = open("session5/TreeHeightProfile.txt", "r")
for element in fobj:
    element= element.strip()
    splitline = element.split("\t")
    x = float(splitline[0])
    y = float(splitline[1])
    z= float(splitline[2])
    treeheight = float(splitline[3])
    Data.append([x,y,z,treeheight])
fobj.close()

Array = np.array(Data)
#print(Array)
#uebung 2 a) 
Array[:,1] = Array[:,1]+3
Array[:,0] = Array[:,0]+4
#print(Array)



numBins = 100
stats = sst.binned_statistic(Array[:,2], Array[:,3], statistic='mean', bins=numBins, range=None)
statsheights = stats[1][0:numBins] #get centre of bin
stats_treeheights = (stats[0]) #get mean of all samples in bin

popt,pcov=curve_fit(fit2,statsheights,stats_treeheights)

residuals = stats_treeheights - fit2(statsheights, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((stats_treeheights-np.mean(stats_treeheights))**2)
r_squared = 1 - (ss_res / ss_tot)
print("R_Squared fit2 :", r_squared) # fits print: 0.873114343762084

popt,pcov=curve_fit(fit3,statsheights,stats_treeheights)

residuals = stats_treeheights - fit3(statsheights, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((stats_treeheights-np.mean(stats_treeheights))**2)
r_squared = 1 - (ss_res / ss_tot)
print("R_Squared fit3: ", r_squared) # fits a bit better Print: 0.8738628719428623

xLine = np.linspace(min(statsheights), max(statsheights), num=1000)
yLine = fit2(xLine,*popt)


plt.plot(statsheights, stats_treeheights,'r.') #'r." steht für Roter punkt ploten
plt.plot(xLine, yLine,'b-') #Blaue linie  
plt.title("Treeheight vs. Terrain Height",fontsize=12)
plt.ylabel('tree height in m')
plt.xlabel('height in m')
plt.savefig("session5/Scatterplot.png",dpi=300)
plt.close()

print("done.")