#Ein programm ist zu schreiben welches alles Werte aus NestedList printed!
NestedList = [[2,3,4],[0,6,1,4],[1,2]]
outlist = []
outlist1 =[]
outlist2 = []
#Inhalt der Liste soll rückwärts ausgegeben werden (ohne reverse() Funktion) --> z.b. mit der Methode inser()

#Ergebnis A 
# 12 0614 234
for i in NestedList:
    #print(i)
    outlist.insert(0,i) #das neue Element wird an erster St elle eingefügt 
    print (outlist)

print (outlist, "Variante A")


# Ergebnis B 
# 432 4160 21
for i in NestedList:
    for j in i:
        #print(j)
        outlist1.insert(0,j)
        #print(outlist1)
    outlist2.insert(0,outlist1)
    outlist1 =[]

print(outlist2,"Variante B")
print ("done.")