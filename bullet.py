import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,settings,screen,player):
        super(Bullet,self).__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.shoot_direction = player.get_shoot_direction()
        self.rect = pygame.Rect(0,0,40,40)
        self.color = settings.bullet_color
        self.rect.x = player.rect.centerx
        self.rect.y = player.rect.centery
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        print(self.shoot_direction)
        if self.shoot_direction["axis"] == "y":
            if self.shoot_direction["direction"] == "up":
                if self.rect.top > 0:
                    self.y -= 5 
            elif self.shoot_direction["direction"] == "bottom":
                if self.rect.bottom < self.screen_rect.bottom:
                    self.y += 5
        
        elif self.shoot_direction["axis"] == 'x':
            if self.shoot_direction["direction"] == "right":
                if self.rect.right < self.screen_rect.right:
                    self.x += 5
            elif self.shoot_direction["direction"] == "left":
                if self.rect.left > 0 :
                    self.x -= 5

        self.rect.x = self.x
        self.rect.y = self.y

def draw(self):
    self.screen.blit(self.screen,self.color,self.rect)
