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

mydist_a = int(input("Geben sie die erste Seitenlänge des Dreiecks ein: "))
mydist_b = int(input("Geben sie die erste Seitenlänge des Dreiecks ein: "))
mydist_c = int(input("Geben sie die erste Seitenlänge des Dreiecks ein: "))


myumfang = mytools.umfang(mydist_a, mydist_b, mydist_c)
myflaeche = mytools.flaeche(mydist_a, mydist_b, mydist_c)

print("Länge 1 ", mydist_a) 
print("Länge 2 ", mydist_c) 
print("länge 3 ",mydist_b)
print("Umfang ", myumfang)
print("Fläche ", myflaeche)



print ("done.")
