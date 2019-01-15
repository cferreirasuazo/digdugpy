import pygame
import os
import sys
from settings import Settings
import game_functions as gf
from player import Player
from pygame.sprite import Group


def start_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Miner by Cristhianxy")
    player = Player(settings, screen)
    bullets = Group()
    ground_grid = Group()
    gf.create_ground(settings,screen,player,ground_grid)

    """MAIN LOOP"""    
    while True:
        
        gf.event_listener(screen,settings,player,bullets)
        player.update()
        gf.update_bullets(settings,screen,bullets)
        gf.update_screen(settings,screen,player,bullets,ground_grid)


start_game()