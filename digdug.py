import pygame
import os
import sys
from settings import Settings
import game_functions as gf



def start_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Miner by Cristhianxy")
    red_surf = pygame.Surface((240,240))
   
    """MAIN LOOP"""    
    while True:
        gf.event_listener()
        gf.update_screen(settings,screen)


start_game()