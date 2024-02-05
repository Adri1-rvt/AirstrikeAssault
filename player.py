"""
Programme python de la classe Player
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT,                                                         vbb                        <p^moipûojmkln b;,nvgfkr'"eé!Adrien RIVET
Version : 1.1
"""

import pygame
from missile import Missile

# créer une classe qui va représenter le joueur
class Player(pygame.sprite.Sprite) :

    def __init__(self) :
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 100
        self.all_missiles = pygame.sprite.Group()
        self.image = pygame.transform.scale(pygame.image.load("assets/boat.png"), (200, 200)) # redimensionner l'image en 200x200

    def lauch_missile(self) :
        # créer une nouvelle instance de la classe Missile
        self.all_missiles.add(Missile(self))
