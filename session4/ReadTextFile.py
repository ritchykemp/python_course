import os
print(os.getcwd())

fobj = open("Session4/TextDatei.txt", "r") #r = read funktion open kennt die Flex 

print(fobj)

nummern = []
namen = []


for element in fobj: 
    #print(element)
    #print(type(element))
    element = element.strip() #reduziert die Einträge um /n (zeichen für zeilenumbruch)
    splitline = element.split(" ")
    #print(splitline)

    Nummer = float(splitline[0]) #macht den datentyp zu einem float (oder int)
    Name = splitline[1]

    #print(Nummer, Name)
    #print(type(Nummer), type(Name))

    nummern.append(Nummer)
    namen.append(Name)
fobj.close()

print(nummern, namen)
fobjout = open("Session4/TextDateiOut.txt", "w") # w = write 

i =1
for element in namen:
    print(element)
    fobjout.write("%s %s\n" % (element,i)) # %s = feses Zeichen (curser) welches von ausen kommt
    # %1.3f = float mit 3 komma stellen
    i+=1
    # \t = tab stop


fobjout.close() #abmelden der schleife / beenden der schelfien
