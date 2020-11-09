"""
Benutzer soll einen Satz eingeben können.
Das Programm soll schauen wie viele Wörter im Satz mit einem Großbuchstaben beginnen.
Es soll die Wörter und die Anzahl der Wörter, welche mit einem Großbuchstaben beginnen ausgeben.
Beispiel:
print(„Im Satz befinden sich …(Anzahl) groß geschrieben Wörter.“)
print(„Diese lauten:“ …) """

upper_word = 0 # zählt alle Groß geschriebene Wörter
upper_words = [] # Kopiert alle groß geschriebenen Wörter

print("Diese Programm gibt an wieviele und welche Wörter in einem Satz groß geschrieben sind.")
x = input("Bitte gib einen Satz ein:").split()
#print("debug: ", x)

for i in x:
    #print("Debug: ",i[0])
    if i[0].isupper() == True:
        upper_word = upper_word +1
        upper_words.append (i)





print("Im Satz befinden sich …", upper_word," groß geschrieben Wörter. ")
print("Diese lauten: ", upper_words)

print ("done.")