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

        #Player Settings
        self.player_speed_factor = 2.102
        self.player_height = 50
        self.player_width = 50
 
        #Bullet settings
        self.bullet_color = (0, 84, 9)
        self.bullet_speed = 25

        #Grid Ground settings
        self.cell_measure = 54
