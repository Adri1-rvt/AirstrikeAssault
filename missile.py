"""
Programme python de la classe Missile
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""


"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame # import de la librairie pygame pour gérer le jeu
import plane # import du fichier plane.py
import time # import de la librairie time pour gérer le temps dans le jeu


"""CORPS DU PROGRAMME"""

# classe qui gère le missile
class Missile(pygame.sprite.Sprite) :
    def __init__(self, player) :
        super().__init__()
        self.velocity = 10 # vitesse du missile
        self.player = player
        self.image = pygame.transform.scale(pygame.image.load("assets/missile_2.png"), (50, 50)) # application de l'image redimensionnée au missile
        self.image = pygame.transform.rotate(self.image, 45) # rotation de l'image du missile
        self.rect = self.image.get_rect() # obtention de la hitbox du missile
        self.rect.x = 325 # position initiale en x du missile
        self.rect.y = 390 # position initiale en y du missile

    # fonction de suppression du projectile (en cas de sortie de l'écran ou collision)
    def remove(self) :
        self.player.all_missiles.remove(self)

    # fonction de gestion de la trajectoire du missile
    def move(self) :
        self.rect.y -= self.velocity # affectation de nouvelle coordonnée en y du missile

        # vérifier si le missile touche un avion
        if self.player.game.check_collision(self, self.player.game.all_planes):
            self.remove() # supprimer le projectile
            for plane in pygame.sprite.spritecollide(self, self.player.game.all_planes, False):
                plane.respawn() # appel de la fonction respawn de plane

        # vérifier que le missile n'est plus présent sur l'écran
        if self.rect.y < 1 :
            self.remove() # supprimer le missile