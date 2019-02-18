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
from start_menu import Menu_Item

def start_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Miner by Cristhianxy")
    game_stats = GameStats(settings)

    menu_items = Group()
    title_top = Menu_Item("MINER",70,screen,50)
    btn_start = Menu_Item("Start",30,screen,135,"start")
    btn_hs = Menu_Item("High Score",30,screen,175,"high_score")
    btn_exit = Menu_Item("EXIT",30,screen,215,"exit")
    sub_title_1 = Menu_Item("Code by Cristhian Ferreira",15,screen,345)
    sub_title_2 = Menu_Item("Created with Pygame and Love",15,screen,380) 

    menu_items.add(title_top,btn_start,btn_hs,btn_start,btn_exit,sub_title_1,sub_title_2)
    


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

                

    """MAIN LOOP"""    
    while True:

        if not game_stats.game_status :
           gf.menu_init(menu_items)
        gf.event_listener(screen,settings,player,bullets,menu_items,game_stats)
      
        if game_stats.game_status:
                        
                player.update()
                #brian.move_y()
                #brian2.move_x()
                gf.update_bullets(settings,screen,bullets)
                gf.update_items(jewels)
                gf.update_screen(settings,screen,player,bullets,ground_grid,monsters,jewels,dashboard,game_stats,dashboard)


start_game()