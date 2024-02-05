"""
Programme python de la class Game
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT,                                                         vbb                        <p^moipûojmkln b;,nvgfkr'"eé!Adrien RIVET
Version : 1.1
"""

import pygame
from player import Player

class Game:
    def __init__(self):
        # générer notre jeu
        self.player = Player()
        self.pressed = {}