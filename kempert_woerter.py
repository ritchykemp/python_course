"""1.)	Aufgabe: alle Selbstlaute zählen (nachname_woerter.py)

Schreibe ein Skript, in dem die Benutzer*innen einen Satz eingeben können.
Das Skript zählt alle vorkommenden Selbstlaute (a,e,i,o,u), und gibt die Anzahl aus.
"""
#ich bin mir nicht sicher ob ä,ü,ö auch als selbstlaute zählen daher habe ich mich an die 5 in der Klammer gehalten. 

#Einleitungssatz 
print("Dieses Skript zählt alle Selbstlaute welche in einem Satz vorkommen ")

#Definition der Variablen
vocale_count = 0 #zählt alle Selbstlaute 
x = input("Bitte gib einen Satz ein: ") #Benutzer*inneneingabe

for i in x:
    #print("DEBUG ",i)
    #Der Satz wird in die einzelnen Zeichen zerlegt
    #Wenn das zeichen einem Selbstlaut entspricht wird die Variable vocale_count um 1 erhöht --> warum
    
    #if i == "a" or "e" or "i" or "o" or "u" --> #funktionierte leider nicht :( weiß nicht warum
    
    if i == "a":  # als workarount alle Selbstlaute einseln abfragen
        #print("DEBUG ",i)
        vocale_count = vocale_count + 1
    elif i =="e":
        vocale_count = vocale_count + 1
    elif i =="i":
        vocale_count = vocale_count + 1
    elif i =="o":
        vocale_count = vocale_count + 1
    elif i =="u":
        vocale_count = vocale_count + 1

#Ergbenis in der Komandozeile ausgeben lassen
print("Der Satz: ", x, "enthält ", vocale_count, "Selbstlaute")
print("done.")