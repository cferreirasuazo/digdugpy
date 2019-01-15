import sys
import pygame
from bullet import Bullet
import traceback
from ground_cell import Ground_cell
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
            print(player.direction)

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

def create_ground(settings,screen,player,ground_grid):
    grain_heigth, grain_width = settings.cell_measure,settings.cell_measure
    player_height = settings.screen_height
    screen_width = settings.screen_width
    screen_height = settings.screen_height
    total_grain_height = int((screen_height / settings.cell_measure ) - (2 * player_height ))
    total_grain_width = int(screen_width / grain_width)
    print(total_grain_width,total_grain_height)

    for x in range(0,50):
        for y in range(0,50):
            cell = Ground_cell(x * 20,y * 20,settings,screen)
            ground_grid.add(cell)
            

    
def update_bullets(settings,screen,bullets):
 
    bullets.update()
    screen_rect = screen.get_rect()
    for bullet in bullets.copy():
        if bullet.shoot_top:
            if bullet.rect.bottom <= 0 :
                print("bullet Removed top")
                bullets.remove(bullet)

        if bullet.shoot_bottom:
            if bullet.rect.top >= screen_rect.bottom :
                print("bullet Removed bottom")
                bullets.remove(bullet)
        
        if bullet.shoot_right:
            if bullet.rect.right >= screen_rect.right:
                bullets.remove(bullet)  

def shoot(settings,screen,player,bullets):
    bullet = Bullet(settings,screen,player)
    bullets.add(bullet)

def update_screen(settings,screen,player,bullets,ground_grid):
    screen.fill(settings.bg_color)

    for bullet in bullets.sprites():
        if bullet.shoot_top or bullet.shoot_bottom or  bullet.shoot_right or bullet.shoot_left:
            bullet.draw()

    for ground_cell in ground_grid.sprites():
        ground_cell.draw()
        
    player.__blit__()
    pygame.display.flip()