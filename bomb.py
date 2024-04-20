import pygame

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/bomb.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        # Déplace la bombe vers le bas
        self.rect.y += 5  # Ajustez la vitesse de la bombe selon vos besoins