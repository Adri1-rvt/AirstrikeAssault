"""
Programme python de la classe Plane
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""

"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame   # import de la librairie pygame pour gérer le jeu
import random   # import de la librairie random pour rendre le jeu un peu aléatoire
from bomb import Bomb   # import de la classe Bomb depuis bomb.py


"""CORPS DU PROGRAMME"""

# classe qui gère les jets
class Plane(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game   # définir game
        self.health = 100   # définir les points de vie du jet
        self.max_health = 100   # définir les points de vie max du jet
        self.image = pygame.transform.scale(pygame.image.load("assets/jet2.png"), (86, 112))    # définir de l'image du jet et de sa taille (en pixels)
        self.image = pygame.transform.rotate(self.image, 90)    # aligner de manière verticale le jet (car jet en diagonal sur l'image)
        self.rect = self.image.get_rect()   # récupérer la hitbox du jet
        self.rect.x = 1200 + random.randint(0, 500)   # définir aléatoirement la position en x du jet
        self.rect.y = 30 + random.randint(0, 200)   # définir aléatoirement la position en y du jet
        self.velocity = 5 + random.randint(0, 10)   # définir aléatoirement la vitesse du jet
        self.initial_position = (self.rect.x, self.rect.y)   # affecter les coordonnées du jet à sa position initiale

    # fonction de respawn du jet éliminé
    def respawn(self):
        self.rect.x = 1200 + random.randint(0, 1000)   # redéfinir aléatoirement la position en x du jet respawn
        self.rect.y = 20 + random.randint(0, 200)   # redéfinir aléatoirement la position en y du jet respawn
        self.health = self.max_health   # réaffecter la vie du jet respawn
        self.game.score += 1   # ajouter 1 au score

    # fonction de lancement de la bombe
    def launch_bomb(self):
        bomb = Bomb(self.game)   # créer une instance de la classe Bomb
        self.game.all_bombs.add(bomb)   # ajouter la bombe au groupe de toutes les bombes du jeu

    # fonction de déplacement du jet
    def forward(self):
        self.rect.x -= self.velocity   # affecter la nouvelle position du jet en fonction de la vitesse pour le faire avancer
        if abs(self.rect.x - 200) < 5:   # si l'avion arrive environ au dessus du bateau
            self.launch_bomb()   # appeler la fonction de lancement de la bombe
        if self.rect.x < -150:   # vérifier que le jet n'est plus présent sur l'écran
            self.respawn()   # supprimer le jet en appelant la fonction respawn