import os
print(os.getcwd())


hights = []
i = 0


fobj = open("Session4/DEM.asc", "r") 
#print(fobj)
for element in fobj: 
    #print(element)
    element = element.strip()
    splitline = element.split(" ")
    #print(splitline[0])
    if (i>5):
        hights.append(splitline)
    i+=1
fobj.close()
#print(hights) #Zeile 6 beginnen die Werte 

high = []

for k in hights:
    for j in k:
        #print(j)
        float(j)
        if j !="-99999.000":
            high.append(j)

print((high[2]))

print("Ausgabe aller Rasterwerte",high)
#print(hights)
print("done.") 