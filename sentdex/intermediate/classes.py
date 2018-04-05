class Mens():
    
    def __init__(self, naam, leeftijd, lengte, gewicht, micro):
        self.naam = naam
        self.leeftijd = leeftijd
        self.lengte = lengte
        self.gewicht = gewicht
        self.micro = int(micro)
    

naam = input("Voer een naam in: ")
leeftijd = input("(in cijfers) Hoe oud is {}? : ".format(naam))
lengte = input("(in cijfers) Hoe lang is {}? : ".format(naam))
gewicht = input("(in cijfers) Hoe zwaar is {}? : ".format(naam))
micro = input('(in hele centimeters) Hoe lang? : ') 
tim = None
tom = None
kees = None
richard = None


persoon = Mens(naam, leeftijd, lengte, gewicht, micro)
persoon.naam = naam
persoon.leeftijd = leeftijd
persoon.lengte = lengte
persoon.gewicht = gewicht
persoon.micro = micro

if int(micro) < 7 or int(micro) == 7:
    print("{} is {} jaar oud, {} meter lang en {} kilo zwaar.".format(naam, leeftijd, lengte, gewicht))
    print("{} heeft een micropenis.".format(naam))
else:
    print("{} is {} jaar oud, {} meter lang en {} kilo zwaar.".format(naam, leeftijd, lengte, gewicht))
    

    
    
    
    