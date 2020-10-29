import math

"""Teil 1
gegeben sind x & y Koordinaten von 3 Punkten
Berechne 
- Seitenlänge (Vektoren!)
- Umfang des Dreiecks
- Fläche des Dreiecks
"""

def dist_a(x1, y1, x2, y2):
    #print ("DEBUG: ", x1, y1, x2, y2, )
    ax =x2 -x1
    ay =y2 -y1
    a = math.sqrt (ax**2 + ay**2)
    print ("DEBUG: a", a)
    return a
def dist_c(x2, y2, x3, y3):
    cx =x3 -x2
    cy =y3 -y2
    c = math.sqrt (cx**2 + cy**2)
    print ("DEBUGG c: ", c)
    return c
def dist_b(x1, y1, x3, y3):
    bx =x3 -x1
    by =y3 -y1
    b = math.sqrt (bx**2 + by**2)
    print ("DEBUG b:", b)
    return b

"""Teil2 - Berechne Umfang """
def umfang(a, b, c,):
    u = a + b + c
    #print ("Der Umfang ist: ", u)
    return u
    

""" Teil3 -Berechne Fläche """
def flaeche(a, b, c):
    s = (a +b +c)/2
    F = math.sqrt (s*(s-a)*(s-b)*(s-c))
    #print ("Die Fläche des Dreiecks ist:", F)
    return F

#MAIN

p1 = int(input("Gib die Erste X Korrdinate ein: "))
b1 = int(input("Gib die Erste Y Korrdinate ein: "))
d2 = int(input("Gib die Zweite X Korrdinate ein: "))
t2 = int(input("Gib die Zweite Y Korrdinate ein: "))  
s3 = int(input("Gib die Dritte X Korrdinate ein: "))
z3 = int(input("Gib die Dritte Y Korrdinate ein: "))

mydist_a = dist_a(p1, b1, d2, t2)
mydist_b = dist_a(p1, b1, s3, z3)
mydist_c = dist_a(d2, t2, s3, z3)

myumfang = umfang(mydist_a, mydist_b, mydist_c)
myflaeche = flaeche(mydist_a, mydist_b, mydist_c)

print("Länge 1 ", mydist_a) 
print("Länge 2 ", mydist_c) 
print("länge 3 ",mydist_b)
print("Umfang ", myumfang)
print("Fläche ", myflaeche)






print("done.")