import pygame.mixer

"""Class for sound handling"""

class SoundPlayer():
    def __init__(self,soundeffect):
        self.soundeffect = soundeffect
            
    def play_sound(self):
        sound = pygame.mixer.Sound(self.soundeffect["soundURL"])
        pygame.mixer.Sound(sound).play().set_volume(self.soundeffect["volume"])

        