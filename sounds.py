import pygame

class SoundManager:
    def __init__(self):
        self.sounds = {
            'click' : pygame.mixer.Sound("assets/sounds/click.ogg",),
            'missile' : pygame.mixer.Sound("assets/sounds/missile.ogg"),
            'game' : pygame.mixer.Sound("assets/sounds/game.mp3"),
            'explosion' : pygame.mixer.Sound("assets/sounds/explosion.wav")
        }

    def play(self, name):
        self.sounds[name].play()