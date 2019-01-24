import pygame
from pygame.sprite import Sprite

class Item(Sprite):
    def __init__(self,screen,settings,x,y,image,points):
        super(Item,self).__init__()
        self.screen = screen
        self.settings = settings
        self.points = points
        self.image =  pygame.image.load(str("assets/" + image))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def __blit__(self):
        self.screen.blit(self.image,self.rect)
        
        