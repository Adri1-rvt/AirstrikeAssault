"""
Programme python de la classe Missile
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT,                                                         vbb                        <p^moipûojmkln b;,nvgfkr'"eé!Adrien RIVET
Version : 1.1
"""

import pygame

# définir la class du missile
class Missile(pygame.sprite.Sprite) :
    def __init__(self, player) :
        super().__init__()
        self.velocity = 10 # vitesse (à ajuster)
        self.player = player
        self.image = pygame.transform.scale(pygame.image.load("assets/missile_2.png"), (50, 50))
        self.image = pygame.transform.rotate(self.image, 45)
        self.rect = self.image.get_rect()
        self.rect.x = 325
        self.rect.y = 390

    # fonction pour supprimer un projectile (en cas de sortie de l'écran ou collision)
    def remove(self) :
        self.player.all_missiles.remove(self)

    def move(self) :
        self.rect.y -= self.velocity

        # vérifier que le missile n'est plus présent sur l'écran
        if self.rect.y < 1 :
            # supprimer le missile
            self.remove()

