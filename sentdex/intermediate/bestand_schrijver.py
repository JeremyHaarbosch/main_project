def schrijf_bestand():
    tekst_bestand = input('Vul hier uw tekst in: ')
    naam_bestand = input('Vul een naam voor een bestand in: ')
    n_bestand = naam_bestand + ".txt"
    nieuw_bestand = open(n_bestand, "w")
    nieuw_bestand.write(tekst_bestand)
    print(f"{naam_bestand} is klaar!")
    
schrijf_bestand()