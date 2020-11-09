a = [1,2,3,4,5]

b = a # b ist nur ein Verweis auf liste a
a.pop() #a & b wurden jeweils um ein Element gekürzt

print(a, b) 

print (id(a),id(b), id(a)==id(b)) #ID´s haben gleiche Ids

#mit Funktion list wird eine element neu erzeugt

c= list(a) # mit list wird eine neue Liste erstellt (ohne attribute --> leere liste )

print (a,c)
print (id(a)==id(c)) #Es sind zwei unterschiedliche Objekte 
a.pop()
print(a,b,c) 