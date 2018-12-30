import sys
import pygame



def event_listener():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings,screen):
    screen.fill(settings.bg_color)
    red_surf = pygame.Surface((50,50))
    red_surf.fill((233,150,122))
    screen.blit(red_surf,(14,150))
    pygame.display.flip()