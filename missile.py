"""
Programme python de la classe Missile
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""

"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame # import de la librairie pygame pour gérer le jeu
import plane # import du fichier plane.py
import time # import de la librairie time pour gérer le temps dans le jeu
import math

"""CORPS DU PROGRAMME"""

screen = pygame.display.set_mode((1280, 667)) # attribuer une taille à la fenetre (en pixels)

# classe qui gère le missile
class Missile(pygame.sprite.Sprite) :
    def __init__(self, player) :
        super().__init__()

        """--------------"""
        self.velocity_x = 10  # Vitesse horizontale initiale du missile
        self.velocity_y = -20  # vitesse verticale initiale du missile
        self.gravity = 0.5  # gravité
        """--------------"""

        self.player = player
        self.image_original = pygame.transform.scale(pygame.image.load("assets/missile_2.png"), (30, 83))
        self.image_original = pygame.transform.rotate(self.image_original, -85)
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect() # obtention de la hitbox du missile

        """--------------"""
        self.rect.x = 325 # position initiale en x du missile
        self.rect.y = 390 # position initiale en y du missile
        """--------------"""

    # fonction de suppression du projectile (en cas de sortie de l'écran ou collision)
    def remove(self) :
        self.player.all_missiles.remove(self)

    # fonction de gestion de la trajectoire du missile
    def move(self) :

        """--------------"""
        self.velocity_y += self.gravity # Mettre à jour la vitesse verticale avec la gravité

        self.rect.y += self.velocity_y # affectation de nouvelle coordonnée en y du missile
        self.rect.x += self.velocity_x  # affectation de nouvelle coordonnée en y du missile

        # Calculer l'angle pour la rotation du missile
        angle = math.degrees(math.atan2(self.velocity_y, self.velocity_x))
        self.image = pygame.transform.rotate(self.image_original, -angle)
        """--------------"""

        # vérifier si le missile touche un avion
        if self.player.game.check_collision(self, self.player.game.all_planes):
            self.remove() # supprimer le projectile
            for plane in pygame.sprite.spritecollide(self, self.player.game.all_planes, False):
                plane.respawn() # appel de la fonction respawn de plane

        # vérifier que le missile n'est plus présent sur l'écran
        if self.rect.y < 1 :
            self.remove() # supprimer le missile