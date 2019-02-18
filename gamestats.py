class GameStats():
    def __init__(self,settings):
        self.high_score = 0
        self.reset_game()
        self.game_status = True
        self.menu_status = True


    def reset_game(self):
        self.score = 0

    def increase_score(self):
        self.score = self.score + 100

    def start_game(self):
        self.game_status = False
        
    

