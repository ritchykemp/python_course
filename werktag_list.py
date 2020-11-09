werktage = ["MO", "Di","Mi", "do", "Fr"]
for i in werktage:
    print(i)

werktage = werktage + ["sa"]
print(werktage, "Werktage + samstag")

werktage.append("So") #ein element hinzufügen
print (werktage, "werktage + sonntag")

werktage.reverse() #dreht die reihenfolge von der liste 
#werktage.sort() #sortiert die Liste (alphabetisch, aufsteigend)
print ("done.")


#Verschachtelte Liste:
mylist= [[1,2],[2,3,4,5],[6,7]]
len(mylist) #anezigen der anzahl der elemente

mylist[2][0] #erster eintrag des letzten Elements 

#Zusamstzfunktionen von Listen

werktage.extend(["tag1","tag2"]) #mehrere Elemente gleichzeitig hinzufügen  durch eine Liste 

print (werktage)