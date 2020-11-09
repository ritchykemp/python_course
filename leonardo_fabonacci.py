"""Die Fibonacci-Folge ist eine unendliche Folge von Zahlen (den Fibonacci-Zahlen), 
bei der sich die jeweils folgende Zahl durch Addition ihrer beiden vorherigen 
Zahlen ergibt: 0, 1, 1, 2, 3, 5, 8, 13..."""

print("das ist die Fabonacci Folge. Du musst nur eine erste Zahl eingeben")



def fibo_list(n): #funktion Fibonacci Folge n ist die Anzahl wie häufig dies passieren soll.
    y = int(input("Gib eine Zahl ein: "))
    fib =[0,y]
    for i in range (1,n):
        fib.append(fib[-1]+fib[-2])
    return fib

#print (fibo_list(100))





"""• Jedes Kaninchenweibchen bringt jeden Monat ein neues Paar zur Welt. 
Junge Kaninchen haben nach einem Monat ihre ersten Jungen. 
Kaninchen sterben nicht. 
Wie viele Kaninchenpaare gibt es nach n Monaten?
1 = 2
2 = 4
3 = 8 usw.
--> es verdoppelt sich jeden Monat
"""


def verdoppelt(n):
    x = int(input("Anzahl der Monate "))
    kan_paar = [1]
    for i in range (1,x):
        kan_paar.append(kan_paar[i-1]*2)
    return kan_paar

print(verdoppelt(5))
print ("done.")



