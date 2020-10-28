#Fakultät in einer schleife Berechnen über eine Schleife
#erste Schleife Usermanagment
"""     Benutzer_in gibt Zahl ein
    Zahl darf nicht negativ sein
    Zahl muss Integer sein
    Wenn 0 eingegeben wird --> script wird beendet """

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

        #zweite Schleife berechnen der fakultät mit for - schleife 
        #vorwärts gerichtet 
        ergebnis = 1
        for i in range(2, zahl+1): #startet mit 2 da sonst wir sonst die mal 1 fakultät doppelt gemacht werden würde  & zahl +1 damit die Zahl auch der eingegebenen Zahl entspricht und nicht zahl-1
            print ("DEBUG", i)
            print (ergebnis, zahl)
            ergebnis = ergebnis *i
        print("ergebnis: ", ergebnis)


print("done.")