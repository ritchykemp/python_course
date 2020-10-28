#Beispiel 1
""" i=1
while i < 10:
    i = i +1
    print (i)
print ("done.")
 """
#Beispiel "Zahlenraten"

#Variablen Definieren
zahl = 12 #richtige Zahl
raten = 0   #geraten Zahl des users 

#Anweisung ausgeben
print ("Gib eine Zahl zwischen 0 und 20 ein, ob du wirklich richtig liegst siehst du was der python ausgibt :) ")

#While schleife
while raten != zahl:
    raten = int(input("Los rate!")) #Input ist immer ein string durch int() vorsatz wird es zum integer 
    # raten = int(raten) --> anderen variante um die input funktion als integer zu speichern
    if raten == zahl and raten > 0 and raten < 100:
        print(raten, "ist richtig!.")
        break
    elif raten <1 or raten > 100:
        print ("Die zahl liegt nicht zwischen 1 und 100 nochmal!")
    else:
        print ("leider flasch")

print ("done.")

