import sys
import pygame

"""Game Modules"""

def listen_press_down(event,settings,player):
        if event.key  == pygame.K_RIGHT:
            player.move_right = True

        if event.key  == pygame.K_LEFT:
            player.move_left = True

        if event.key  == pygame.K_UP:
            player.move_up = True
        
        if event.key  == pygame.K_DOWN:
            player.move_down = True

def listen_press_up(event,player):
        if event.key  == pygame.K_RIGHT:
            player.move_right = False
        if event.key  == pygame.K_LEFT:
            player.move_left = False
        if event.key  == pygame.K_UP:
            player.move_up = False        
        if event.key  == pygame.K_DOWN:
            player.move_down = False

def event_listener(settings,player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            listen_press_up(event,player)
        if event.type == pygame.KEYDOWN:
            listen_press_down(event,settings,player)

def update_screen(settings,screen,player):
    screen.fill(settings.bg_color)
    player.__blit__()
    pygame.display.flip()