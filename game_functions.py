import sys
import pygame
from bullet import Bullet
import traceback
from ground_cell import Ground_cell
from item import Item
import time 
import threading
import datetime
"""Game Modules"""

def listen_press_down(event,screen,settings,player,bullets):
     
        if event.key  == pygame.K_RIGHT :
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

def event_listener(screen,settings,player,bullets,menu_items,game_stats):
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            listen_press_up(event,player)
        if event.type == pygame.KEYDOWN:
            listen_press_down(event,screen,settings,player,bullets)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            for item in menu_items.sprites():
                clicked = item.title_rect.collidepoint(x,y)
                if clicked:
                    if item.task == "start":
                        game_stats.start_game()
                        

def menu_init(menu_items):
        for item in menu_items.sprites():
            item.draw()
        pygame.display.flip()



def remove_jewel(jewels,jewel,game_stats,sb):
    time.sleep(0.1)
    if jewels.has(jewel):
        jewels.remove(jewel)
        game_stats.increase_score()
        sb.prep_score()
        
    
def player_jewel_collide(player,jewels,ground_grid,game_stats,sb):
        
        for jewel in jewels.sprites():
           if not pygame.sprite.spritecollideany(jewel,ground_grid):
                collision =  pygame.sprite.spritecollideany(player,jewels)
        
                if collision:

                    t = threading.Thread(target=remove_jewel, args = (jewels,jewel,game_stats,sb))
                    t.start()

def remove_cells(monsters,ground_grid):
    pygame.sprite.groupcollide(monsters,ground_grid,False,True)

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
    for x in range(15,45):
        x = x * 20
        for y in range(15,35):
            y = y * 20
            cell = Ground_cell(x,y,settings,screen)
            ground_grid.add(cell)

    for item in ground_grid.sprites():
        if item.rect.x == 400 and item.rect.y == 520:
            ground_grid.remove(item)

        if item.rect.x == 400 and item.rect.y == 500:
            ground_grid.remove(item)
          
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

def update_screen(settings,screen,player,bullets,ground_grid,monsters,jewels,dashboard,game_stats,sb):
    screen.fill(settings.bg_color)

    dashboard.__blit__()

    check_ground_collition(ground_grid,player)
    player_jewel_collide(player,jewels,ground_grid,game_stats,sb)
    remove_cells(monsters,ground_grid)

    for bullet in bullets.sprites():
        if bullet.shoot_top or bullet.shoot_bottom or  bullet.shoot_right or bullet.shoot_left:
            bullet.draw()

    for item in jewels.sprites():
      item.draw()

    for ground_cell in ground_grid.sprites():  
        ground_cell.draw()

    for monster in monsters.sprites():
        monster.__blit__()
        
    player.__blit__()
    
    pygame.display.flip()