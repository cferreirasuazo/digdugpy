import pygame
import os
import sys
from settings import Settings
import threading
import game_functions as gf
from player import Player
from pygame.sprite import Group
from monster import Monster
from item import Item
from dashboard import Dashboard
from gamestats import GameStats
from start_menu import Menu

def start_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Miner by Cristhianxy")
    game_stats = GameStats(settings) 
    menu = Menu(screen,settings)


    player = Player(settings, screen)
    bullets = Group()
    ground_grid = Group()
    jewels = Group()
    gf.create_ground(settings,screen,player,ground_grid)
    brian = Monster(settings,screen,400,500)
    brian2 = Monster(settings,screen,500,400)
    monsters = Group()
    monsters.add(brian,brian2)
    gf.create_jewels(screen,settings,jewels)
    game_stats.reset_game()
    dashboard = Dashboard(screen,settings,game_stats)
    #game_stats.start_game()
    

#     thread = threading.Thread(target=gf.menu_init, args=(menu,))
#     thread.start()
                

    """MAIN LOOP"""    
    while True:
        gf.menu_init(menu)
        gf.event_listener(screen,settings,player,bullets,menu)
      
        if game_stats.game_status:
                        
                player.update()
                #brian.move_y()
                #brian2.move_x()
                gf.update_bullets(settings,screen,bullets)
                gf.update_items(jewels)
                gf.update_screen(settings,screen,player,bullets,ground_grid,monsters,jewels,dashboard,game_stats,dashboard)


start_game()