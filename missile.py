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
        self.velocity_x = 10 # vitesse du missile

        """--------------"""
        self.velocity_y = -20  # vitesse verticale initiale du missile
        self.gravity = 0.5  # gravité
        """--------------"""

        self.player = player
        self.image_original = pygame.transform.scale(pygame.image.load("assets/missile_2.png"), (30, 83))
        self.image_original = pygame.transform.rotate(self.image_original, -85)
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect() # obtention de la hitbox du missile
        self.rect.x = 325 # position initiale en x du missile
        self.rect.y = 390 # position initiale en y du missile

    # fonction de suppression du projectile (en cas de sortie de l'écran ou collision)
    def remove(self) :
        self.player.all_missiles.remove(self)

    # fonction de gestion de la trajectoire du missile
    def move(self) :
        self.velocity_y += self.gravity


        self.rect.y += self.velocity_y # affectation de nouvelle coordonnée en y du missile
        self.rect.x += self.velocity_x  # affectation de nouvelle coordonnée en y du missile

        angle = math.degrees(math.atan2(self.velocity_y, self.velocity_x))
        self.image = pygame.transform.rotate(self.image_original, -angle)

        # vérifier si le missile touche un avion
        if self.player.game.check_collision(self, self.player.game.all_planes):
            self.explode()
            self.remove() # supprimer le projectile
            for plane in pygame.sprite.spritecollide(self, self.player.game.all_planes, False):
                plane.respawn() # appel de la fonction respawn de plane

        # vérifier que le missile n'est plus présent sur l'écran
        if self.rect.y < 1 :
            self.remove() # supprimer le missile

    def explode(self):
        explosion_image = pygame.image.load('assets/explosion_2.png')
        explosion_image = pygame.transform.scale(explosion_image, (125, 125))
        explosion_rect = explosion_image.get_rect()
        explosion_rect.center = self.rect.center

        # Sauvegarder les coordonnées du missile avant de le supprimer
        missile_position = self.rect.topleft

        # Ajouter un décalage de pixels vers le haut
        missile_position = (missile_position[0] + 100, missile_position[1] - 150)

        explosion_rect.center = missile_position

        # Afficher l'explosion pendant 1 seconde
        screen.blit(explosion_image, missile_position)
        pygame.display.flip()
        pygame.time.delay(250)  # Pause d'une seconde pour afficher l'explosion

        # Effacer l'explosion après 1 seconde
        background = pygame.image.load("assets/background.png")  # affection l'image de l'arrière plan
        screen.blit(background, explosion_rect, explosion_rect)
        pygame.display.flip()