""" Teil 1
Überprüfung von Benutzereingabe ob es sich um einen Strick handelt
dafür soll die try / except & die Funktion int() verwednet werden """

#Benutzereingabe
x = input("Bitte gib ein String ein: ")

#Kontrolle ob es ein string ist
for i in x :
    #print("DEBUG: ", i)
    try:
        print ("jawohl das ist ein STring :) ")
                
    except:
        y = int(i)
        print("Das ist Kein String")



""" Teil 2
umwandelung der String benutzereingabe und ausgabe 
- Großbuchstaben in Kleinbuchstaben 
- Kleinbuchstaben in Großbuchstaben

Dafür benutzen einer FOR schleife & folgende String - Funktionen
- str.islower()
- str.isupper()
- str.upper()
- str.lower()
"""
#so ist es glaub ich leichter zu lösen :)
#print (x.swapcase())

swapstring = ""

for i in x: 
# Checking for lowercase letter and converting to uppercase. 
    if (i.isupper()) == True: 
        swapstring+=(i.lower()) 
# Checking for uppercase letter and converting to lowercase. 
    elif (i.islower()) == True: 
        swapstring+=(i.upper()) 

  
print("After changing cases:") 
print(swapstring) 

print ("done.")