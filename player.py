import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self,settings,screen):
        super(Player,self).__init__()
        self.settings = settings
        self.screen = screen
        self.player_color = (3, 32, 79)
        self.surface = pygame.Surface((75,75))
        self.surface.fill(self.player_color)
        self.rect = self.surface.get_rect()
        self.rect.x ,self.rect.y = 100,100

    def __blit__(self):
        print("CALLIN BLIT")
        self.screen.blit(self.surface,self.rect)