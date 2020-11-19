import math
from operator import itemgetter

def MEAN_temperatur(n):
    x = sum(n)/len(n)
    return x



#Übung 3 Monatswerte_wetterstaion.txt einlesen --> 
#Programm soll Daten der Wetterstaion einlesen für Zeitraum 2005-2010 (6 Jahre ) folgende WErte Berechene
# Summe Niederschläge RSS

#Arbeitsvariablen festlegen


data = []
result_list = []
sum_temp = []

fobj = open("Session4/monatswerte_wetterstation.txt", "r") 
#print(fobj)
for element in fobj: 
    #print(element[1])
    element = element.strip()
    splitline = element.split(";")
    #print(splitline)
    data.append(splitline)
    #for i in splitline:
        #print(i)
fobj.close()

data.pop(0)
data.pop(0)
data.pop(0)

#Summe Niederschlag liste
sum_rain = []

#print(data[0])
for i in data:
    datum = int(i[1])
    rain = float(i[10])
    temp = float(i[5])
    #print(datum, rain) 
    if (datum>200412) and (datum<201001):
        sum_rain.append(rain) #Niederschlagsmenge Listen Erstellen zum aufsummieren
        mypairs = [datum, rain, temp] #Tupels in dennen Das datum mit der Niederschlagsmenge & Temperatur gespeichert sind 
        result_list.append(mypairs) #Tupels an Liste anhängen 
        sum_temp.append(temp)
        

res_rain = sorted(result_list, key= itemgetter(1)) #sortieren der Liste nach dem Niederschlagswerten
#print("Der Monat mit dem geringsten Niederschlag:",res_rain[0][0])

#Monat mit geringstene Niederschlägen abkürzung RSS
low_rain = res_rain[0][0]
low_rain_value = res_rain[0][1]

res_temp = sorted(result_list, key= itemgetter(2)) #sortiere Liste nach der Temperatur
#print("Der Monat mit der geringsten Temperatur",res_temp[0][0])
#print("Der Monat mit der höchsten Temperatur",res_temp[len(res_temp)-1][0])

#Monat mit niedrigstne Temperatur (+ ausgabe des niedrigsten wertes ) TMM
low_temp = res_temp[0][0]
low_temp_value = res_temp[0][2]
#Monat mit höchsten Temperatur (+ ausgabe des höchsten wertes) TMM
high_temp = res_temp[len(res_temp)-1][0]
high_temp_value = res_temp[len(res_temp)-1][2]


#Eigen Funktion  Mittelwert monatliche Durchschnittstemperatur
mean_temp = 0
#print(sum_temp)
#mean_temp = sum(sum_temp)/len(sum_temp)
#print(mean_temp)
mean_temp = MEAN_temperatur(sum_temp)




#Ergebnis in textfile schreiben 
fobj_out = open("Session4/uebung3_ausgabe.txt", "w")
fobj_out.write("%1.0f mm Summe aller Niederschläge\n%1.0f Monat mit Höchste Temperatur im Zeitraum%1.2f°C\n%1.0f Monat mit der Niedrigste Temperatur %1.2f°C\n%1.0f  Monat mit geringster Regenmenge %1.2f in mm \n%1.2f °C Durschnittstemperatur der Monate \n" %(sum(sum_rain), high_temp ,high_temp_value,low_temp,low_temp_value ,low_rain, low_rain_value,mean_temp))
fobj_out.close()