import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    def __init__(self,settings,screen,x,y):
        super(Monster,self).__init__()
        self.settings = settings
        self.screen = screen 
        self.screen_rect = self.screen.get_rect()
        self.player_color = (3, 32, 79)
        self.surface = pygame.Surface((30,30))
        self.surface.fill(self.settings.monster_color)
        self.rect = self.surface.get_rect()
        self.rect.x ,self.rect.y = x,y
        self.x ,self.y = (self.rect.x), (self.rect.y)
        self.destiny_number = 50
        self.destiny_right = self.rect.x + self.destiny_number
        self.destiny_left = self.rect.x - self.destiny_number

        self.destiny_top = self.rect.y +self.destiny_number
        self.destiny_bottom = self.rect.y  - self.destiny_number
        self.direction_right = "right"
        self.direction_top = "top"
        


    def move_x(self):
        
        if self.direction_right == "right":
            if self.rect.x < self.destiny_right:
                self.x = self.x + 1
            else:
               self.direction_right = "left"

        else:
            if self.rect.x > self.destiny_left:
                self.x = self.x - 1
            else:
                self.direction_right = "right"

        self.rect.x = self.x
     

    def move_y(self):
     

        if self.direction_top == "top":
            if self.rect.y < self.destiny_top:
                self.y = self.y + 1
            else:
               self.direction_top = "bottom"

        else:
            if self.rect.y > self.destiny_bottom:
                self.y = self.y - 1
            else:
                self.direction_top = "top"

        self.rect.y = self.y


    def __blit__(self):       
        self.screen.blit(self.surface,self.rect)