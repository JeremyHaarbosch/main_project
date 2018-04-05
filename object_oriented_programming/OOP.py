import pygame
from blop import Blop

START_RODE_BLOPS = 3
START_blauwE_BLOPS = 10



breedte = 800
hoogte = 600
wit = (255,255,255)
blauw = (0,0,255)
rood = (255,0,0)

game_beeld = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption('Blop Wereld')
klok = pygame.time.Clock()

def teken_omgeving(blop_lijst):
    game_beeld.fill(wit)
    
    for blop_dict in blop_lijst:
        for blop_id in blop_dict:
            blop = blop_dict[blop_id]
            pygame.draw.circle(game_beeld, blop.kleur, [blop.x, blop.y], blop.grootte)
            blop.move()
    pygame.display.update() 
        
def main():
    blauwe_blops = dict(enumerate([Blop(blauw, hoogte, breedte) for i in range(START_blauwE_BLOPS)]))
    rode_blops = dict(enumerate([Blop(rood, hoogte, breedte) for i in range(START_RODE_BLOPS)]))
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        teken_omgeving([blauwe_blops, rode_blops])
        klok.tick(60)
        
if __name__ == '__main__':
    main()