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
        self.items.add(Item("MINER",30,self.frame,10))
        self.items.add(Item("NEW GAME",30,self.frame,10))
        self.items.add(Item("High Score",30,self.frame,45))
        self.items.add(Item("EXIT",30,self.frame,80))
        self.items.add(Item("Code by Cristhian Ferreira",15,self.frame,115))
        self.items.add(Item("Created with Pygame and Love",20,self.frame,140))
        
       
        

    def draw(self):
        self.screen.blit(self.frame,self.rect_frame)
        for item in self.items.sprites():
            item.draw()
            print(item.title_font)



class Item(Sprite):
    def __init__(self,title,size,surface,y):
        super(Item,self).__init__()
        self.surface = surface
        self.surface_rect = self.surface.get_rect()
        self.title_font = font.Font("assets/font/arcade_n.ttf",size)
        self.title_text = self.title_font.render(title,True,(255, 255, 255),(0, 0, 0))
        self.title_rect = self.title_text.get_rect()
        self.coord_x = int((self.surface_rect.width - self.title_rect.width)/ 2 )
        self.y = y

    def draw(self):
        self.surface.blit(self.title_text,(self.coord_x,self.y))



        
