""" Teil 1
Überprüfung von Benutzereingabe ob es sich um einen Strick handelt
dafür soll die try / except & die Funktion int() verwednet werden """

#Benutzereingabe
x = input("Bitte gib ein String ein: ")

#Kontrolle ob es ein string ist
for i in x :
    print("DEBUG: ", i)
    try:
        y = int(i)
        print("Das ist Kein String")
    except:
        print ("jawohl das ist ein STring :) ")
        


""" Teil 2
umwandelung der Strgin benutzereingabe und ausgabe 
- Großbuchstaben in Kleinbuchstaben 
- Kleinbuchstaben in Großbuchstaben

Dafür benutzen einer FOR schleife & folgende String - Funktionen
- str.islower()
- str.isupper()
- str.upper()
- str.lower()
"""

print ("done.")