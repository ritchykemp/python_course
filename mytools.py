import math

def calcfacult(var): 
    ergebnis = 1
    for i in range(2, var+1): #startet mit 2 da wir sonst die mal 1 fakultät doppelt gemacht werden würde & zahl +1 damit die Zahl auch der eingegebenen Zahl entspricht und nicht zahl-1
        #print ("DEBUG", i)
        print (ergebnis, var)
        ergebnis = ergebnis *i
        print ("DEBUG", ergebnis)
    return ergebnis #speichert das Resultat in der variable ergebnis

"""Berechne Seitenlänge von Dreiecken mit Korrdinaten von 3 Punkten"""
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

"""Berechne Umfang """
def umfang(a, b, c,):
    u = a + b + c
    #print ("Der Umfang ist: ", u)
    return u
    

"""Berechne Fläche """
def flaeche(a, b, c):
    s = (a +b +c)/2
    F = math.sqrt (s*(s-a)*(s-b)*(s-c))
    #print ("Die Fläche des Dreiecks ist:", F)
    return F