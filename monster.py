import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    def __init__(self,settings,screen,x,y):
        super(Monster,self).__init__()
        self.settings = settings
        self.screen = screen 
        self.screen_rect = self.screen.get_rect()
        self.player_color = (3, 32, 79)
        self.surface = pygame.Surface((50,50))
        self.surface.fill(self.settings.monster_color)
        self.rect = self.surface.get_rect()
        self.rect.x ,self.rect.y = x,y
        self.x ,self.y = (self.rect.x), (self.rect.y)
        self.destiny_right = self.rect.x + 200
        self.destiny_left = self.rect.x - 200

        self.destiny_top = self.rect.y + 200
        self.destiny_bottom = self.rect.y  - 200
        self.direction_right = "right"
        self.direction_top = "top"
        # self.move_right = False
        # self.move_left = False
        # self.move_up = False
        # self.move_down = False


    # def update(self):
    #     if self.move_right and self.rect.right < self.screen_rect.right:
    #         self.x += self.settings.player_speed_factor

    #         self.direction_right = "right"
    #     if self.move_left and self.rect.left > 0 :
    #         self.x -= self.settings.player_speed_factor
            
    #         self.direction_right = "left"
    #     if self.move_up and self.rect.top > 0 :
    #         self.y -= self.settings.player_speed_factor
            
    #         self.direction_right = "top"
    #     if self.move_down and self.rect.bottom < self.screen_rect.bottom:
    #         self.y += self.settings.player_speed_factor
    #         self.direction_right = "bottom"

    #     self.rect.x = self.x
    #     self.rect.y = self.y


    def move_x(self):
        print("MOVING MONSTER X")

        if self.direction_right == "right":
            if self.rect.x < self.destiny_right:
                self.x = self.x + 5
            else:
               self.direction_right = "left"

        else:
            if self.rect.x > self.destiny_left:
                self.x = self.x - 5
            else:
                self.direction_right = "right"

        self.rect.x = self.x
     

    def move_y(self):
        print("MOVING MONSTER Y")

        if self.direction_top == "top":
            if self.rect.y < self.destiny_top:
                self.y = self.y + 5
            else:
               self.direction_top = "bottom"

        else:
            if self.rect.y > self.destiny_bottom:
                self.y = self.y - 5
            else:
                self.direction_top = "top"

        self.rect.y = self.y


    def __blit__(self):       
        self.screen.blit(self.surface,self.rect)