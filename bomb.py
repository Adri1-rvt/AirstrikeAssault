"""
Programme python de la classe Bomb
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""

import pygame

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))  # Créez une surface rectangulaire pour représenter la bombe
        self.image.fill((255, 0, 0))  # Remplissez la surface en rouge (vous pouvez changer la couleur selon vos préférences)
        self.rect = self.image.get_rect()  # Obtenez le rectangle entourant l'image de la bombe
        self.speed = 5  # Vitesse de chute de la bombe

    def move(self):
        self.rect.y += self.speed  # Faites descendre la bombe en Y

        # Si la bombe atteint le bas de l'écran, supprimez-la
        if self.rect.y > 667:  # 667 est la hauteur de votre écran, ajustez-la si nécessaire
            self.kill()  # Supprimez la bombe du groupe lorsque sa position Y dépasse la hauteur de l'écran

