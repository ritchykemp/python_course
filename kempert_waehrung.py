"""2.)	Aufgabe Währungsrechner (nachname_waehrung.py)

Schreibe ein Skript, das einen vom Benutzer*innen eingegebenen 
Betrag der drei Währungen EUR, USD, YEN wahlweise in die beiden anderen 
Währungen umrechnen kann (also EUR  USD, YEN; USD  EUR, YEN; YEN  EUR, USD).
Tipp:	Verwende dabei die Umrechnungskurse der Seite 
https://www.umrechner-euro.de/ezb-wechselkurse
"""
#Einelitungssatz:
print("Dieses Skript ist ein kleiner Währungsrechner")

#definition der Variablen
EUR = "Euro"
USD = "Doller"
YEN = "Yen"
    #Umrechnungskurs euro in die anderen
eu = 1.1808
ey = 124.36
    #Umrechnungskurs usd in die anderen
ue = 0.85
uy = 105.32
    #umrechnungskurs yen in die anderen 
ye = 0.01
yu = 0.0095

while True:
    #Benutzer*innen eingabe der Währung & des Betrages 
    waehrung = input("Bitte gib die Währung ein du kannst wählen zwischen -Euro- -Doller- -Yen- ")
    betrag = int(input("Bitte gib den Betrag ein den du umrechnen willst :  "))

    if waehrung == EUR:
        print("DEBUG", waehrung)
        print("Der Eingegebene Betrag ", betrag, "in ", EUR, "wären", betrag * eu, USD, "und", betrag * ey, YEN)
        break
    elif waehrung == USD:
        print ("DEBUG", waehrung)
        print("Der Eingegebene Betrag ", betrag, "in ", USD, "wären", betrag * ue, EUR, "und", betrag * uy, YEN)
        break
    elif waehrung == YEN:
        print ("DEBUG,", waehrung)
        print("Der Eingegebene Betrag ", betrag, "in ", YEN, "wären", betrag * ye, EUR, "und", betrag * yu, USD)
        break
    else:
        print("Das war leider keine Währung, probiere es nochmal")
        continue









print("done.")