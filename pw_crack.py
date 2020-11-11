#Posswort cracker 
"""Schreibe ein Python Script, welches versucht ein vom User angegebenes Passwort zu knacken. 
Das Programm hat unendlich viele Versuche.
• Das ganze soll über einen “Brute-Force-Ansatz” passieren, 
bei dem alle Kombinationen getestet werden, bis es passt.
• Das eingegebene Passwort sollte eine festgelegte Länge von 2 (4) Zeichen haben.
• Es kann alle englischen Buchstaben (groß und klein), 
alle arabischen Zahlen , “_”, “!” und “?” enthalten.
• Wieviele Kombinationen gibt es ? """

pw = "2hr3"
leng_pw =len(pw)
possible= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_!?"
#print (len(possible)) 
x = len(possible) #65 mögliche Zeichen
#print(comb)

comb = x**leng_pw

print("Kombinationsmöglichkeiten für das aktuelle Passwort: ", comb)
#bei 2 Zeichen 4225 optionen
#bei 4 Zeichen 17850625 optionen


#Teil2 Brute-Force- Cracker:

password = input("Gib ein Passwort mit 4 Zeichen ein: ")
for i1 in possible:
    for i2 in possible:
        for i3 in possible: 
            for i4 in possible:
                password2 = i1+i2+i3+i4
                if password2 == password:
                    print(" Das passwort lautet :",password2)
                    break
                #else:
                    #print(password2)
            if password2 == password:
                break
        if password2 == password:
                break
    if password2 == password:
                break



print("done.")


