import pygame
from pygame.sprite import Sprite
import pygame.font as font
from pygame.sprite import Group


class Menu():
    def __init__(self,screen,settings):
        self.settings = settings
        self.screen = screen
        self.frame = pygame.Surface((700,500))
        self.frame.fill((0,0,0))
        self.rect_frame = self.frame.get_rect()
        self.rect_frame.x = int((self.settings.screen_width - self.rect_frame.width) / 2) 
        self.rect_frame.y = int((self.settings.screen_height - self.rect_frame.height) / 2) 
        self.items = Group()
        self.items.add(Item("MINER",70,self.frame,50))
        self.items.add(Item("NEW GAME",30,self.frame,135,"new_game"))
        self.items.add(Item("High Score",30,self.frame,175,"high_score"))
        self.items.add(Item("EXIT",30,self.frame,215,"exit"))
        self.items.add(Item("Code by Cristhian Ferreira",15,self.frame,345))
        self.items.add(Item("Created with Pygame and Love",15,self.frame,380))
       
    def draw(self):
        self.screen.blit(self.frame,self.rect_frame)
        for item in self.items.sprites():
            item.draw()



class Item(Sprite):
    def __init__(self,title,size,surface,y,task = ""):
        super(Item,self).__init__()
        self.surface = surface
        self.title = title
        self.task = task
        self.surface_rect = self.surface.get_rect()
        self.title_font = font.Font("assets/font/arcade_n.ttf",size)
        self.prep_text()
        self.title_rect = self.title_text.get_rect()
        self.coord_x = int((self.surface_rect.width - self.title_rect.width)/ 2 )
        self.y = y

    def draw(self):
        self.surface.blit(self.title_text,(self.coord_x,self.y))


    def prep_text(self,color = (255, 255, 255) ):
         self.title_text = self.title_font.render(self.title,True,color,(0, 0, 0))




        
