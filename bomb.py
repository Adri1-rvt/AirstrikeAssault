"""
Programme python de la classe Bomb
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""

"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame   # importer la bibliothèque pygame pour gérer le jeu


"""CORPS DU PROGRAMME"""

class Bomb(pygame.sprite.Sprite):   # classe de la bombe, qui hérite de la classe Sprite de pygame
    def __init__(self, game):   # appeler le constructeur de la classe parente (Sprite)
        super().__init__()
        self.game = game   # initialiser l'instance de la classe Game, permettant d'accéder aux attributs et méthodes de Game
        self.image = pygame.transform.scale(pygame.image.load("assets/bomb.png"), (50, 83))   # attribuer une image pour notre bombe
        self.rect = self.image.get_rect()   # obtenir la hitbox de la bombe
        self.rect.y = 50   # positionner la bombe relativement en haut de l'écran
        self.speed = 4   # paramétrer la vitesse de chute de la bombe