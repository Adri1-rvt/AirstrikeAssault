"""
Programme python de la classe Plane
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""


"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame # import de la librairie pygame pour gérer le jeu
import random # import de la librairie random pour créer des évènements aléatoires


"""CORPS DU PROGRAMME"""

# classe qui gère les jets
class Plane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100 # points de vie du jet
        self.max_health = 100 # points de vie maximum du jet
        self.attack = 5 # points d'attaque du jet
        self.image = pygame.transform.scale(pygame.image.load("assets/jet.png"), (150, 150)) # définition de l'image du jet et de sa taille (en pixels)
        self.image = pygame.transform.rotate(self.image, 135) # alignement vertical du jet (car jet en diagonal sur l'image)
        self.rect = self.image.get_rect() # récupération de la hitbox du jet
        self.rect.x = 1200 + random.randint(0, 500) # définition aléatoire de la position en x du jet
        self.rect.y = 20 + random.randint(0, 100) # définition aléatoire de la position en y du jet
        self.velocity = 5 + random.randint(0, 5) # définition aléatoire de la vitesse du jet
        self.initial_position = (self.rect.x, self.rect.y) # affectation des coordonnées du jet à sa position initiale

    # fonction de respawn du jet éliminé
    def respawn(self):
        self.rect.x = 1200 + random.randint(0, 500) # redéfinition aléatoire de la position en x du jet respawn
        self.rect.y = 20 + random.randint(0, 100) # redéfinition aléatoire de la position en y du jet respawn
        self.health = self.max_health # réaffectation de la vie du jet respawn

    # fonction de déplacement du jet
    def forward(self):
        self.rect.x -= self.velocity # affectation de la nouvelle position du jet en fonction de la vitesse pour le faire avancer

        # vérifier que le jet n'est plus présent sur l'écran
        if self.rect.x < -150:
            # supprimer le jet en appelant la fonction respawn
            self.respawn()

        if self.rect.x == 500:
            print("Shooter")
