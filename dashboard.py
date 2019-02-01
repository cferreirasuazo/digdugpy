import pygame
import pygame.font as font

class Dashboard():
    def __init__(self,screen,settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()
        self.score_font = font.Font("assets/font/arcade_n.ttf",30)
        self.hs_font = font.Font("assets/font/arcade_n.ttf",35)

        #Board Surface & Rect
        self.board_surface = pygame.Surface((self.screen_rect.width, 100))
        self.board_surface.fill(self.settings.bg_color)
        self.board_rect = self.board_surface.get_rect()
        self.board_rect.x = (self.screen_rect.width - self.board_surface.get_rect().width ) / 2
        self.board_rect.y = 0

        self.title_high_score(10)
        self.prep_high_score(self.title_high_score_rect.bottom + 10)
        self.prep_score(110,self.title_high_score_rect.bottom + 10)
       
       

    def __blit__(self):
        self.screen.blit(self.board_surface,self.board_rect)
        self.board_surface.blit(self.score_img,self.score_rect)
        self.board_surface.blit(self.high_score_img,self.high_score_rect)
        self.board_surface.blit(self.title_high_score_img,self.title_high_score_rect)


    def prep_score(self,x,y):

        #Score Surface & Rect

        score_str = str("00000")
        self.score_img = self.score_font.render(score_str,True,
                                            self.settings.board_font_color,
                                            self.settings.board_bg_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.x = x
        self.score_rect.y = y#int((self.board_rect.height - self.score_rect.height ) / 2)

    def prep_high_score(self,y):
              
        #HighScore Surface 
        high_score_str = str("0")
        self.high_score_img = self.hs_font.render(high_score_str,True,
                                            self.settings.board_font_color,
                                            self.settings.board_bg_color)
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.x = int((self.board_rect.width - self.high_score_rect.width) / 2)
        self.high_score_rect.y = y

    def title_high_score(self,y):
              
        #HighScore Surface 
        title_high_score_str = str("HIGHSCORE")
        self.title_high_score_img = self.hs_font.render(title_high_score_str,True,
                                            self.settings.board_font_color,
                                            self.settings.board_bg_color)
        self.title_high_score_rect = self.title_high_score_img.get_rect()
        self.title_high_score_rect.x = int((self.board_rect.width - self.title_high_score_rect.width) / 2)
        self.title_high_score_rect.y = y



