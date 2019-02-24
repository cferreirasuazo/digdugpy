import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,settings,screen,player):
        super(Bullet,self).__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0,0,40,40)
        self.color = settings.bullet_color
        self.rect.x = player.rect.centerx + (-21)
        self.rect.y = player.rect.centery + (-21)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.shoot_top = False
        self.shoot_bottom = False
        self.shoot_right = False
        self.shoot_left = False
        self.direction = player.direction
        self.set_bullet_direction(player.direction)
        
       
    def set_bullet_direction(self,direction):
        
        if direction == "top":
            self.shoot_top = True
        if direction == "bottom":
            self.shoot_bottom = True
        if direction == "right":
            self.shoot_right = True
        if direction == "left":
            self.shoot_left = True



    def update(self):
        if self.shoot_top:    
            self.y -= self.settings.bullet_speed
            self.rect.y = self.y

        if self.shoot_bottom:
            self.y += self.settings.bullet_speed
            self.rect.y = self.y
        
        if self.shoot_right:
            self.x += self.settings.bullet_speed
            self.rect.y = self.x

        if self.shoot_left:
            self.x -= self.settings.bullet_speed
            self.rect.x = self.x

        
        self.rect.x = self.x
        self.rect.y = self.y




    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
