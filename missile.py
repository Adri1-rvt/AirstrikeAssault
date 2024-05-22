"""
Programme python de la classe Missile
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""

"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame   # import de la librairie pygame pour gérer le jeu
import math   # import de la librairie maths pour utiliser des outils mathématiques


"""CORPS DU PROGRAMME"""

screen = pygame.display.set_mode((1280, 667))   # attribuer une taille à la fenetre (en pixels)

# classe qui gère le missile
class Missile(pygame.sprite.Sprite) :
    def __init__(self, player) :
        super().__init__()

        """--------------"""
        self.velocity_x = 10   # définir la vitesse horizontale initiale du missile
        self.velocity_y = -20  # définir la vitesse verticale initiale du missile
        self.gravity = 0.5  # définir la gravité
        """--------------"""

        self.player = player   # définir player
        self.image_original = pygame.transform.scale(pygame.image.load("assets/missile_2.png"), (30, 83))   # définir et transformer l'image du missile
        self.image_original = pygame.transform.rotate(self.image_original, -85)   # transformer l'angle de l'image
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect()   # obtenir la hitbox du missile

        """--------------"""
        self.rect.x = 325   # définir la position initiale en x du missile (en pixels)
        self.rect.y = 390   # définir la position initiale en y du missile (en pixels)
        """--------------"""

    # fonction de suppression du missile (en cas de sortie de l'écran ou collision)
    def remove(self) :
        self.player.all_missiles.remove(self)   # supprimer le missile

    # fonction de gestion de la trajectoire du missile
    def move(self) :

        """--------------"""
        self.velocity_y += self.gravity   # mettre à jour la vitesse verticale en fonction de la gravité

        self.rect.y += self.velocity_y   # affecter la nouvelle coordonnée en y du missile
        self.rect.x += self.velocity_x   # affecter la nouvelle coordonnée en y du missile

        # calculer l'angle pour la rotation du missile
        angle = math.degrees(math.atan2(self.velocity_y, self.velocity_x))
        self.image = pygame.transform.rotate(self.image_original, -angle)
        """--------------"""

        if self.player.game.check_collision(self, self.player.game.all_planes):   # vérifier si le missile touche un avion
            self.remove()   # supprimer le projectile
            for plane in pygame.sprite.spritecollide(self, self.player.game.all_planes, False):
                plane.respawn()   # appeler la fonction respawn de plane
        if self.rect.y < 1 :   # vérifier que le missile n'est plus présent sur l'écran
            self.remove()   # supprimer le missile