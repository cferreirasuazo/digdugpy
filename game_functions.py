import sys
import pygame

"""Game Modules"""

def event_listener():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings,screen,player):
    screen.fill(settings.bg_color)
    player.__blit__()
    #red_surf = pygame.Surface((75,75))
    #red_surf.fill((3, 32, 79))
    #x,y = 100,100
    #screen.blit(red_surf,(x,y))
    pygame.display.flip()