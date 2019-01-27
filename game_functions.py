import sys
import pygame
from bullet import Bullet
import traceback
from ground_cell import Ground_cell
from item import Item
import time 
import threading
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


def remove_play_sound(jewels,jewel):
    time.sleep(0.5)
    jewels.remove(jewel)
    print("PLAY SOUND")

def jewels_point(player,jewels,ground_grid):

        collided = pygame.sprite.groupcollide(jewels,ground_grid,False,False)
        
        for jewel in jewels.sprites():
           if not pygame.sprite.spritecollideany(jewel,ground_grid):
               if pygame.sprite.spritecollideany(player,jewels):
                  t = threading.Thread(target=remove_play_sound, args = (jewels,jewel))
                  t.start()
               
        # collided = pygame.sprite.spritecollideany(player,jewels)
        
        # if collided:
        #     print("collied")
        #     jewels.remove(collided)

def create_jewels(screen,settings,jewels):
        jewel_list = [
            ["jewel_blue.png",5],
            ["jewel_purple.png",10],
            ["jewel_yellow.png",3]
        ]

        jewels.add(Item(screen,settings,380,440,jewel_list[0][0],jewel_list[0][1]))
        jewels.add(Item(screen,settings,580,480,jewel_list[0][0],jewel_list[0][1]))
        jewels.add(Item(screen,settings,360,480,jewel_list[1][0],jewel_list[1][1]))
        jewels.add(Item(screen,settings,740,380,jewel_list[1][0],jewel_list[1][1]))
        jewels.add(Item(screen,settings,580,540,jewel_list[2][0],jewel_list[2][1]))
        jewels.add(Item(screen,settings,480,640,jewel_list[2][0],jewel_list[2][1]))
                
def create_ground(settings,screen,player,ground_grid):
    grain_heigth, grain_width = settings.cell_measure,settings.cell_measure
    player_height = settings.player_height
    screen_width = settings.screen_width
    screen_height = settings.screen_height
    for x in range(15,45):
        x = x * 20
        for y in range(15,35):
            y = y * 20
            cell = Ground_cell(x,y,settings,screen)
            ground_grid.add(cell)
          


def check_ground_collition(ground_grid,player):
    collited = pygame.sprite.spritecollideany(player,ground_grid)     
    
    if collited:
        ground_grid.remove(collited)
        
def update_bullets(settings,screen,bullets):
 
    bullets.update()
    screen_rect = screen.get_rect()
    for bullet in bullets.copy():
        if bullet.shoot_top:
            if bullet.rect.bottom <= 0 :
                bullets.remove(bullet)

        if bullet.shoot_bottom:
            if bullet.rect.top >= screen_rect.bottom :
                bullets.remove(bullet)
        
        if bullet.shoot_right:
            if bullet.rect.right >= screen_rect.right:
                bullets.remove(bullet)  

def shoot(settings,screen,player,bullets):
    bullet = Bullet(settings,screen,player)
    bullets.add(bullet)

def update_screen(settings,screen,player,bullets,ground_grid,monsters,jewels):
    screen.fill(settings.bg_color)
    check_ground_collition(ground_grid,player)

   

    for jewel in jewels.sprites():
        jewel.__blit__()

    jewels_point(player,jewels,ground_grid)

    for bullet in bullets.sprites():
        if bullet.shoot_top or bullet.shoot_bottom or  bullet.shoot_right or bullet.shoot_left:
            bullet.draw()

    for ground_cell in ground_grid.sprites():
         ground_cell.draw()
        
    player.__blit__()
    
    # for monster in monsters.sprites():
    #     monster.__blit__()
    
    pygame.display.flip()