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

        #zweite Schleife berechnen der fakultät mit while 
        """ rückwärts beginnend z.b. bei 4! zuerst 4 dann 4 *3 dann 4 *3 *2 dann 4*3 *2 *1 dann stopp """
        ergebnis = 1
        while zahl > 0: # es wird solange  die zahl um 1 reduziert bis die zahl = 1 
            print (ergebnis, zahl)
            ergebnis = ergebnis * zahl #starten mit der eingegebenen zahl ( im zweiten durchlauf multiplizieren mit der reduzierten zahl )
            zahl = zahl - 1 # zahl reduzieren um eins 
        print ("Ergebnis: ", ergebnis)

print ("done.")