import math
#Übung 2
print ("Uebung 2 Hypothenuse & Volumen Berechnen")
#variablen definieren (kateten)
k1 = 3.4
k2 = 9.1

h = math.sqrt(k1**2 + k2**2) #hypothenusen berechnen

#Ausgabe der hypothenuse im terminal 
print ("Hypothenuse", h)

#Variablen
r = 5 #radius

v = 4/3 * math.pi *r**3 #Berechnen Volumen

print ("Volumen Kugel", v)

print("done.")