#Aufgabe ist es einen Taschenrechner zu programmieren
# + - * / wollen möglich sein 
#zwei Zahlen eingeben (welche dann mathematisch operiert werden)
# Programm gibt ergebnis aus

pl = "+"
mi = "-"
mu = "*"
ge = "/"
ergebnis = 0

while True:
    zahl1 = int(input("Geben sie die erste Zahl ein: "))
    zahl2 = int(input("Geben sie die zweite Zahl ein:"))

    operator = input("Geben sie einen Mathematischen Operator ein. Die Möglichkeiten sind: + - * /: ")

    if operator == pl:
        print("debug", operator)
        ergebnis = zahl1 + zahl2
        break
    elif operator == mi:
        ergebnis = zahl1 - zahl2
        break
    elif operator == mu:
        ergebnis = zahl1 * zahl2
        break
    elif operator == ge:
        ergebnis = zahl1/zahl2
        break
    else:
        print("Das war kein Operator nochmal")
        continue

print("Das Ergebniss von: ", zahl1, operator, zahl2, "=", ergebnis)
print("done.")