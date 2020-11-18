import os
print(os.getcwd())

fobj = open("Session4/TextDatei.txt", "r")

print(fobj)

for element in fobj: 
    print(element)