#Import Module
import random
import time

t1 = time.time()
#print(t1)


#Zufallszahlen
zufallslist = []
for i in range (1000):
    a = int(random.random()*1000)
    zufallslist.append(a)

t2 = time.time()
#Variante For Schleife
result=[]
for i in zufallslist:
    c = zufallslist.count(i)
    mytuple = (i,c)
    if result.count(mytuple)== 0:
        result.append(mytuple)
#print (result)
t3 = time.time()

#Variante Dictionary
result_dic = {}
for i in zufallslist:
    c = zufallslist.count(i)
    mytuple = (i,c)
    result2 = []
    result2.append(mytuple)
    #print(result2)
    result_dic.update(result2)
t4 = time.time()
#result_dic.update(zufallslist)
#print("Ausgabe der Zufallsliste", result_dic)
 


t12 = t2-t1
t23 = t3-t2
t34 = t4-t3
print("zeit für for-schleife", t23)
print("Zeit für dictionary", t34)
print("done.")