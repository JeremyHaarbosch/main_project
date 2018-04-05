# krijg aantal rijen voor boom
boom_hoogte = input("hoe hoog is de boom?: ")

# verander in integer
boom_hoogte = int(boom_hoogte)

# spaties voor boom
spaties = boom_hoogte - 1

# er is een hekje om te starten, om bij te voegen
hekjes = 1

# sla spaties op
stam_spaties = boom_hoogte - 1

# print aantal rijen
while boom_hoogte != 0:
    
# print (unknown)
    for i in range(spaties):
        print(' ', end="")

# nieuwe lijn na elke rij
    for i in range(hekjes):
        print(' ', end="")

# spaties -= 1
    spaties -= 1

# hekjes += 2
    spaties += 2

    for i in range(stam_spaties):
        print(' ', end="")
    
print("#")