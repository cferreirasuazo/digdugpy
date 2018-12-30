import pygame
import os
import sys
from settings import Settings
import game_functions as gf
from player import Player


def start_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Miner by Cristhianxy")
    player = Player(settings, screen)

    """MAIN LOOP"""    
    while True:
        gf.event_listener()
        gf.update_screen(settings,screen,player)


start_game()