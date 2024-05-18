"""
Programme python de la classe Game
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""
from sounds import SoundManager

"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame  # import de la librairie pygame pour gérer le jeu
from player import Player  # import de la classe Player depuis player.py
from plane import Plane  # import de la classe Plane depuis plane.py
from config import missile_fire_rate  # import du taux de tir de missile depuis config.py
import time

"""CORPS DU PROGRAMME"""

# classe qui gère le jeu
class Game:
    def __init__(self):
        # définir si le jeu a commencé
        self.is_playing = False
        # générer notre jeu
        self.player = Player(self)
        # groupe de jet
        self.all_planes = pygame.sprite.Group()
        self.pressed = {}
        # Groupe pour gérer toutes les bombes du jeu
        self.all_bombs = pygame.sprite.Group()
        self.score = 0
        self.police = pygame.font.Font("assets/font/font.ttf", 25)
        self.sound_manager = SoundManager()

    def start(self):
        self.is_playing = True
        self.spawn_plane()

    def game_over(self):
        self.all_planes = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0

    def update(self, screen):
        # afficher le score
        score_text = self.police.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquer l'image du bateau
        screen.blit(self.player.image, (200, 420))

        # récupérer les projectiles du joueur
        for missile in self.player.all_missiles:
            missile.move()

        # récupérer les avions
        for plane in self.all_planes:
            plane.forward()

            # Vérifier la collision entre les missiles et les avions
            for missile in self.player.all_missiles:
                if pygame.sprite.collide_rect(missile, plane):
                    missile.explode()  # Appel de la fonction d'explosion du missile
                    self.sound_manager.play('explosion')
                    plane.respawn()  # Appel de la fonction respawn de l'avion
                    missile.remove()  # Supprimer le missile

        # appliquer l'ensemble des images du groupe de missiles
        self.player.all_missiles.draw(screen)

        # appliquer l'ensemble des images du groupe de jets
        self.all_planes.draw(screen)

        # mise à jour de l'écran
        pygame.display.flip()

        # Dessiner et déplacer les bombes
        for bomb in self.all_bombs:
            screen.blit(bomb.image, (bomb.rect.x, bomb.rect.y))
            bomb.move()

    # fonction de gestion des collisions
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # fonction de spawn des jets
    def spawn_plane(self):
        plane = Plane(self)  # Passer la référence au jeu lors de la création de l'instance de Plane
        self.all_planes.add(plane)