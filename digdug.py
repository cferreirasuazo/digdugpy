import pygame
import os
import sys
from settings import Settings
import game_functions as gf
from player import Player
from pygame.sprite import Group
from monster import Monster


def start_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Miner by Cristhianxy")
    player = Player(settings, screen)
    bullets = Group()
    ground_grid = Group()
    gf.create_ground(settings,screen,player,ground_grid)
    brian = Monster(settings,screen,400,500)
    brian2 = Monster(settings,screen,500,400)

    monsters = Group()
    monsters.add(brian,brian2)

    """MAIN LOOP"""    
    while True:
        
        gf.event_listener(screen,settings,player,bullets)
        player.update()
        brian.move_y()
        brian2.move_x()
        gf.update_bullets(settings,screen,bullets)
        gf.update_screen(settings,screen,player,bullets,ground_grid,monsters)


start_game()