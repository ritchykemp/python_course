#uebung 5 - Schaltjahprüfung


#Regeln für Schaltjahr --> Aufgabe: ist Jahr XX ein schaltjahr? Ergebnis in Terminal ausgeben
#ist Schaltjarh wenn:
    # X >1582
    # X teilbar 4 & NICHT teilbar durch 100
    # Oder X ist teilbar durch 400 

print ("Mit diesem kleinem Programm kannst du herausfinden welches Jahr ein Schaltjahr war.")
#Eingabe des jahres
x = int(input("Gib das gewünscht Jahr ein: "))
if x%400 ==0 and x>1582 and x<2020:
    print ("Das Jahr", x, "ist ein Schaltjahr gewesen")
elif x%400 ==0 and x>2020:
    print ("Das Jahr", x, "wird ein Schaltjahr sein")
elif x%4 ==0 and x%100 !=0 and x>1582 and x<2020:
    print ("Das Jahr", x, "ist ein Schaltjahr gewesen")
elif x%4 ==0 and x%100 !=0 and x>2020:
    print ("Das Jahr", x, "wird ein Schaltjahr sein")
elif x%4 !=0:
    print ("Das Jahr",x ,"war kein Schaltjahr")
else:
    print ("Das Jahr", x, "wird Kein Schaltjahr sein")

print('done.')