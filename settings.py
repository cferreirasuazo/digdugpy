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
        self.player_measure = 23.3

        self.player_speed_factor = 1.2345
        self.player_height = self.player_measure
        self.player_width = self.player_measure
 
        #Bullet settings
        self.bullet_color = (0, 84, 9)
        self.bullet_speed = 25

        #Grid Ground settings
        self.cell_measure = 19.5
        self.cell_color = (255,0,0)

        #Monster Prototype

        self.monster_color = (214, 23, 166)

        #Scoreboard 
        self.board_bg_color = (0, 0, 0)
        self.board_font_color = (244, 244, 244)
