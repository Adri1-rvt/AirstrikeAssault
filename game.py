"""
Programme python de la classe Game
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""


"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame # import de la librairie pygame pour gérer le jeu
from player import Player # import de la classe Player depuis player.py
from plane import Plane # import de la classe Plane depuis plane.py


"""CORPS DU PROGRAMME"""

# classe qui gère le jeu
class Game:
    def __init__(self):
        # générer notre jeu
        self.player = Player(self)
        # groupe de jet
        self.all_planes = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_plane()
        # Groupe pour gérer toutes les bombes du jeu
        self.all_bombs = pygame.sprite.Group()

    # fonction de gestion des collisions
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # fonction de spawn des jets
    def spawn_plane(self):
        plane = Plane(self)  # Passer la référence au jeu lors de la création de l'instance de Plane
        self.all_planes.add(plane)
