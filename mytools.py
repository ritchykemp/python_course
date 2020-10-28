def calcfakult(var): 
    ergebnis = 1
    for i in range(2, zahl+1): #startet mit 2 da wir sonst die mal 1 fakultät doppelt gemacht werden würde & zahl +1 damit die Zahl auch der eingegebenen Zahl entspricht und nicht zahl-1
        #print ("DEBUG", i)
        print (ergebnis, zahl)
        ergebnis = ergebnis *i
        print ("DEBUG", ergebnis)
    return ergebnis #speichert das Resultat in der variable ergebnis