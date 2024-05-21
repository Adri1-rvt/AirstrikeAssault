"""
Programme python de la classe Game
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""

"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame  # import de la librairie pygame pour gérer le jeu
from player import Player  # import de la classe Player depuis player.py
from plane import Plane  # import de la classe Plane depuis plane.py
from config import missile_fire_rate  # import du taux de tir de missile depuis config.py
import time
from sounds import SoundManager

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
        self.all_bombs = pygame.sprite.Group()

    def start(self):
        self.is_playing = True
        self.spawn_plane()
        self.spawn_plane()

    def game_over(self):
        screen = pygame.display.set_mode((1280, 667))
        # Afficher l'image "Game Over" pendant 5 secondes
        game_over_image = pygame.image.load("assets/game_over.png")
        game_over_image = pygame.transform.scale(game_over_image, (screen.get_width(), screen.get_height()))

        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 5000:  # 5000 millisecondes = 5 secondes
            screen.blit(game_over_image, (0, 0))
            score_text = self.police.render(f"Score : {self.score}", 1, (0, 0, 0))
            screen.blit(score_text, (20, 20))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        self.all_planes = pygame.sprite.Group()
        self.all_bombs = pygame.sprite.Group()
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
                    self.sound_manager.play('explosion')
                    plane.respawn()  # Appel de la fonction respawn de l'avion
                    missile.remove()  # Supprimer le missile

        # appliquer l'ensemble des images du groupe de missiles
        self.player.all_missiles.draw(screen)

        # appliquer l'ensemble des images du groupe de jets
        self.all_planes.draw(screen)

        for bomb in self.all_bombs:
            screen.blit(bomb.image, (300, bomb.rect.y))
            bomb.rect.y += bomb.speed  # Déplacer la bombe vers le bas

            # vérifier si la bombe atteint le milieu de l'écran
            if bomb.rect.y >= screen.get_height() // 1.75:
                bomb.kill()  # supprimer la bombe si elle atteint le milieu de l'écran
                self.player.damage()

                pygame.display.flip()

    # fonction de gestion des collisions
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # fonction de spawn des jets
    def spawn_plane(self):
        plane = Plane(self)  # Passer la référence au jeu lors de la création de l'instance de Plane
        self.all_planes.add(plane)