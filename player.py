"""
Programme python de la classe Player
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""


"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame # import de la librairie pygame pour gérer le jeu
from missile import Missile # import de la classe Missile depuis missile.py


"""CORPS DU PROGRAMME"""

# classe qui gère le joueur
class Player(pygame.sprite.Sprite) :

    def __init__(self, game) :
        super().__init__()
        self.game = game
        self.health = 100 # points de vie du joueur
        self.max_health = 100 # points de vie maximum du joueur
        self.attack = 100 # points d'attaque du joueur
        self.all_missiles = pygame.sprite.Group()
        self.image = pygame.transform.scale(pygame.image.load("assets/boat.png"), (200, 200)) # redimensionner l'image en 200x200 et affecter l'image

    def lauch_missile(self) :
        # créer une nouvelle instance de la classe Missile
        self.all_missiles.add(Missile(self))
