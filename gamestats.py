class GameStats():
    def __init__(self,settings):
        self.high_score = 0
        self.reset_game()


    def reset_game(self):
        self.score = 0

    def increase_score(self):
        self.score = self.score + 100

