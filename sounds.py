"""
Programme python de la classe SoundManager
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""

"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame


"""CORPS DU PROGRAMME"""

# classe qui gère le sound manager
class SoundManager:
    def __init__(self):
        self.sounds = {   # créer un dict de sons
            'click' : pygame.mixer.Sound("assets/sounds/click.ogg",),
            'missile' : pygame.mixer.Sound("assets/sounds/missile.ogg"),
            'game' : pygame.mixer.Sound("assets/sounds/game.mp3"),
            'explosion' : pygame.mixer.Sound("assets/sounds/explosion.wav")
        }

    # fonction de lancement d'un son
    def play(self, name):
        self.sounds[name].play()   # jouer le son