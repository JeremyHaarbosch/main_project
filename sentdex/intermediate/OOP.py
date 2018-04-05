import pygame
import random

START_RODE_BLOPS = 10
START_BLAUWE_BLOPS = 3



WIDTH = 800
HEIGHT = 600
WIT = (255,255,255)
BLAUW = (0,0,255)
ROOD = (255,0,0)


game_beeld = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blop Wereld')
klok = pygame.time.Clock()


class Blop:

    def __init__(self, kleur):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4, 8)
        self.kleur = kleur
    def move(self):
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_y
        
        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = WIDTH
        
        if self.y < 0: self.y = 0
        elif self.y > HEIGHT: self.y = HEIGHT


def teken_omgeving(blops):
    game_beeld.fill(WIT)
    for blop_id in blops:
        blop = blops[blop_id]
        pygame.draw.circle(game_beeld, blop.kleur, [blop.x, blop.y], blop.size)
        blop.move()
    pygame.display.update() 
        
def main():
    blauwe_blops = dict(enumerate([Blop(BLAUW) for i in range(START_BLAUWE_BLOPS)]))
    print(blauwe_blops)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        teken_omgeving(blauwe_blops)
        klok.tick(60)
        
if __name__ == '__main__':
    main()