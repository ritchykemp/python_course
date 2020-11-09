#neues Dictionary anliegen

mitarbeitende = {}
etage = {60705: 7, 60632:6, 60544:5}
magnus = {"phone": "5075428", "Mail": "magnus.bremer@uibk.ac.at", "room": 60705}
martin = {"phone": "123456", "Mail:":"martin.rutzinger@uibk.ac.at", "room:": 60632}

#fill in dictionary
mitarbeitende["Bremer"] = magnus 
mitarbeitende["Rutzinger"] =martin 

#print(mitarbeitende)
#print(etage)
#print(magnus)

#ABFRAGE
print("telefonnummer Magnus Bremer", mitarbeitende["Bremer"]["phone"])
roomnumber = mitarbeitende["Rutzinger"]["room:"]
print("Etage von martin rutzinger", etage[roomnumber])

print("done.")