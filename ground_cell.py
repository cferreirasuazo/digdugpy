import pygame
from pygame.sprite import Sprite
import traceback

class Ground_cell(Sprite):
    def __init__(self,x,y,settings,screen):
        #traceback.print_stack()
        super(Ground_cell,self).__init__()
        self.screen = screen
        self.settings = settings
        self.color = self.settings.cell_color
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("assets/ground.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):

        self.screen.blit(self.image,self.rect)

