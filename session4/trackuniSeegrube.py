

import math
import os
print(os.getcwd())
def Compute_Distance(x1,y1,x2,y2):
	Dist = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
	return Dist

fobj = open("Session4/TrackUniSeegrube.txt", "r") #r = read funktion open kennt die Flex 

points = []
i = 0
for element in fobj: 
    
    element = element.strip() 
    splitline = element.split("\t")
    #print(splitline)

    if(i>0):
        Name = splitline[0]
        x = float(splitline[1])
        y= float(splitline[2])
        z= float(splitline[3])
        #print (x,y,z)
        points.append((x,y,z)) #erzeugt zusammenhängends tuple 
    i+=1
fobj.close()

fobjout = open("Session4/TrackUniSeegrube_Distanz.txt", "w")
#print(points)
dist_sum = 0
for i in range(1,len(points)):
    x2 = points[i][0]
    y2 = points[i][1]
    x1 = points[i-1][0]
    y1 = points[i-1][1]
    dist = Compute_Distance(x1,y1,x2,y2)
    
    dist_sum+=dist
    print (dist, dist_sum)
    fobjout.write("%1.1f %1.1f %1.3f m  %1.3f m\n" %(x1,x2,dist,dist_sum))

fobjout.close()

print("done.")