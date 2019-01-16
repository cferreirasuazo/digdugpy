import pygame
from pygame.sprite import Sprite
from pygame.gfxdraw import circle

class Player(Sprite):
    def __init__(self,settings,screen):
        super(Player,self).__init__()
        self.settings = settings
        self.screen = screen 
        self.screen_rect = self.screen.get_rect()
        self.player_color = (3, 32, 79)
        self.surface = pygame.Surface((self.settings.player_width,self.settings.player_height))
        self.surface.fill(self.player_color)
        self.rect = self.surface.get_rect()
        self.rect.x ,self.rect.y = 100,100
        self.x ,self.y = (self.rect.x), (self.rect.y)
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        self.direction = "bottom"

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed_factor

            self.direction = "right"
        if self.move_left and self.rect.left > 0 :
            self.x -= self.settings.player_speed_factor
            
            self.direction = "left"
        if self.move_up and self.rect.top > 0 :
            self.y -= self.settings.player_speed_factor
            
            self.direction = "top"
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.player_speed_factor
            self.direction = "bottom"

        self.rect.x = self.x
        self.rect.y = self.y

    def __blit__(self):       
        self.screen.blit(self.surface,self.rect)