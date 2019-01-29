import pygame

class Dashboard():
    def __init__(self,screen,settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()

        #Board Surface & Rect
        self.board_surface = pygame.Surface((900, 100))
        self.board_surface.fill((228, 127, 0))
        self.board_rect = self.board_surface.get_rect()
        self.board_rect.x = (self.screen_rect.width - self.board_surface.get_rect().width ) / 2
        self.board_rect.y = 10

        self.prep_score()
        self.prep_high_score()

    def __blit__(self):
        self.screen.blit(self.board_surface,self.board_rect)
        self.board_surface.blit(self.score_surface,self.score_rect)
        self.board_surface.blit(self.high_score_surface,self.high_score_rect)


    def prep_score(self):

        #Score Surface & Rect
        self.score_surface = pygame.Surface((100,35))
        self.score_surface.fill((35, 168, 152))
        self.score_rect = self.score_surface.get_rect()
        self.score_rect.x = 150
        self.score_rect.y = int((self.board_rect.height - self.score_rect.height ) / 2)

    def prep_high_score(self):
              
        #HighScore Surface 
        self.high_score_surface =  pygame.Surface((100,75))
        self.high_score_surface.fill((43, 173, 60))
        self.high_score_rect = self.high_score_surface.get_rect()
        self.high_score_rect.x = int((self.board_rect.width - self.high_score_rect.width) / 2)
        self.high_score_rect.y = 0



