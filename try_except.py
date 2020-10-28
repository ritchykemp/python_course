#beispiel mit try except

a ="1 2 3 4 5"

for var in a:
    # print ("DEBUG: ", var)
    try:
        x = int(var)
        y = x*2
        print (y)
    except:
        print("Warnung - kann nicht konvertiert werden")
print ("done.")
