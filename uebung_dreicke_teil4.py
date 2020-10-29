import math
import mytools

"""Teil 4
Usereingabe und Schleife
- Programmiere User Eingabe für Seitenlängen 
- & Schrittweite sowie Schrittzahl #range

Das Programm berechnet Längen, Umfang, Fläche in einer Schleife 
- Berechneten Längen in jeder Iteration um die Schrittweite erhöht wird
- Iterationen so häufig bis vom USER angegebene Schrittanzahl errreicht ist
"""
#Usereingabe für Seitlenlänge
a = int(input("Geben sie die erste Seitenlänge des Dreiecks ein: "))
b = int(input("Geben sie die erste Seitenlänge des Dreiecks ein: "))
c = int(input("Geben sie die erste Seitenlänge des Dreiecks ein: "))

#print("Länge 1 ", a) 
#print("Länge 2 ", c) 
# print("länge 3 ", b)


#Benutzereingabe der Schrittzahl und Schrittweite 
step_wide = int(input("Geben sie die Schrittweite ein in welcher die Seitenlänge vergrößert werden soll: "))
step_count = int(input("Geben sie ein wie häufig die Seitenlänge um die Schrittweite vergrößert werden soll: "))

#For Schleife die die Vergrößerung des Umfangs errechnet
for i in range (0, step_count*step_wide + 1, step_wide):
    mydist_a = a + i
    mydist_b = b + i
    mydist_c = c + i
    myumfang = mytools.umfang(mydist_a, mydist_b, mydist_c)
    myflaeche = mytools.flaeche(mydist_a, mydist_b, mydist_c)
    print("Seitenlängen des Dreiecks: ", mydist_a, mydist_b, mydist_c, )
    print("Dazu passender Umfang ", myumfang)
    print("Dazu passende Fläche ", myflaeche)
    #mydist_a = mydist_a + step_wide

print ("done.")
