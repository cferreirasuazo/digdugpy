import pygame
from pygame.sprite import Sprite

class Item(Sprite):
    def __init__(self,screen,settings,x,y,image = None):
        super(Item,self).__init__()
        self.rect = pygame.image.load()
        