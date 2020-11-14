#Dictionary mit Vorname & Telefonnummer

tel = {"martin": 4012, "franz": 3636} #dic erstellen
tel["peter"] = 4444 # eintrag hinzufügen
print(tel)

del tel["martin"]
print(tel)

#alle keys abfragen
print(tel.keys())

#existiert ein bestimmter key in einem dictionary
print("martin" in tel)

#Ausgabe aller keys in einer for schleife
for i in tel:
    print (i)

#ausgabe aller werte
for i in tel:
    print (tel[i])

print("done.")
