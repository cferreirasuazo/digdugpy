import pygame

class Settings():
    def __init__(self):
        self.bg_color = (0,0,0)
        #get information of the display
        winObject = pygame.display.Info()
        #gets height of the screen
        self.screen_height =  winObject.current_h - int(winObject.current_h * 0.10 )
        #gets width of the screen
        self.screen_width = winObject.current_w - int(winObject.current_w * 0.10 )
