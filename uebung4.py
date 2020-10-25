#uebung 4 __passwort eingabe 
# testing ob passwort richtig ist
# 3 Versuche passwort einzugeben

#Passwort
pw = "GeHeiM"
"""count = 0
while count < 3:
    var = input("Bitte das Passwort eingeben: ")
    if var == pw:
        print ("Hallo User")
        break #stoping this loop
    else:
        print ("WRONG!!")
        count+=1 


print ('done.') """

#mögliche Andere Lösung:
# using for loop 

for i in range (3, 0, -1):
    trie = input("Bitte das Passwort eingeben: ")
    if trie == pw:
        print ("Hallo User")
        break #stoping this loop
    else:
        print ("WRONG!!")
if i == 1:
    print("No access for you!")
else:
    print( "Hello User ")     
