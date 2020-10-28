#Fakultät in einer schleife Berechnen über eine Schleife
import mytools
#FUNCTION
""" def fakultaet(var): #definition der Funktion!
    ergebnis = 1
    for i in range(2, zahl+1): #startet mit 2 da sonst wir sonst die mal 1 fakultät doppelt gemacht werden würde  & zahl +1 damit die Zahl auch der eingegebenen Zahl entspricht und nicht zahl-1
        #print ("DEBUG", i)
        print (ergebnis, zahl)
        ergebnis = ergebnis *i
        print ("DEBUG", ergebnis)
    return ergebnis #speichert das Resultat in der variable ergebnis
#Berechnen der Fakultät """


#Main (Haupatprogramm)
while True: #nur ergebnis der Bedingung wird angegeben (endlos schleife)
    zahl = int(input("Geben sie eine Zahl ein: "))
    if zahl < 0:
        print ("Negative Zahl sind nicht erlaubt")
        continue #startet wieder von Vorn
    elif zahl == 0:
        print ("Das Programm wird beendet.")
        break # beendet das Programm
    else:
        print (zahl, "gültige Eingabe.")
        #Funktionsaufruf
        myresult = mytools.calcfacult(zahl)

        print ("FOR Schleife: Fakultät von: ", zahl, "=", myresult)
print("done.")