"""
Programme python de la classe Bomb
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""

"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame


"""CORPS DU PROGRAMME"""

class Bomb(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load("assets/bomb.png"), (50, 83))
        self.rect = self.image.get_rect()
        self.rect.y = 50  # Positionnez la bombe en haut de l'écran
        self.speed = 4  # Vitesse de déplacement de la bombe vers le bas