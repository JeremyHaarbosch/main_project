##BELANGRIJKE FUNCTIES (IMPORTEER ALTIJD)
import csv
naam_bestand = "asdf"
#lees bestand(csv)
def lees_bestand():
	n_bestand = naam_bestand + ".txt"
	with open(n_bestand, "r") as nieuw_bestand:
 		data_bestand = csv.reader(nieuw_bestand)
 		for lijst in data_bestand:
 	 		print(' '.join(lijst))
lees_bestand()
