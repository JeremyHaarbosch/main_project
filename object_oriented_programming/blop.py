import random

class Blop:

    def __init__(self, kleur, breedte, hoogte, grootte_reeks=(4,8), beweging_reeks=(-1,2)):
        self.grootte = random.randrange(grootte_reeks[0], grootte_reeks[1])
        self.kleur = kleur
        self.breedte= breedte
        self.hoogte = hoogte
        self.x = random.randrange(0, breedte)
        self.y = random.randrange(0, hoogte)
        self.beweging_reeks = beweging_reeks
        
    def move(self):
        self.move_x = random.randrange(self.beweging_reeks[0], self.beweging_reeks[1])
        self.move_y = random.randrange(self.beweging_reeks[0], self.beweging_reeks[1])
        self.x += self.move_x
        self.y += self.move_y
        
        if self.x < 0: self.x = 0
        elif self.x > self.breedte: self.x = self.breedte
        
        if self.y < 0: self.y = 0
        elif self.y > self.hoogte: self.y = self.hoogte

