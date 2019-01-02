import sys
import pygame
from bullet import Bullet
"""Game Modules"""

def listen_press_down(event,screen,settings,player,bullets):
        if event.key  == pygame.K_RIGHT:
            player.move_right = True

        if event.key  == pygame.K_LEFT:
            player.move_left = True

        if event.key  == pygame.K_UP:
            player.move_up = True
        
        if event.key  == pygame.K_DOWN:
            player.move_down = True

        if event.key == pygame.K_SPACE:
            shoot(settings,screen,player,bullets)


def listen_press_up(event,player):
        if event.key  == pygame.K_RIGHT:
            player.move_right = False
        if event.key  == pygame.K_LEFT:
            player.move_left = False
        if event.key  == pygame.K_UP:
            player.move_up = False        
        if event.key  == pygame.K_DOWN:
            player.move_down = False

def event_listener(screen,settings,player,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            listen_press_up(event,player)
        if event.type == pygame.KEYDOWN:
            listen_press_down(event,screen,settings,player,bullets)

def update_bullets(settings,screen,bullets):
    print("UPDATING BULLET")
    screen_rect = screen.get_rect()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0 or bullet.rect.top >= screen_rect.top or bullet.rect.right < screen_rect.right or bullet.rect.left > 0:
            bullets.remove(bullet)

def shoot(settings,screen,player,bullets):
    bullet = Bullet(settings,screen,player)
    bullets.add(bullet)

def update_screen(settings,screen,player):
    screen.fill(settings.bg_color)
    player.__blit__()
    pygame.display.flip()