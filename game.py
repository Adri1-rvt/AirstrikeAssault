"""
Programme python de la classe Game
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""

"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame   # import de la librairie pygame pour gérer le jeu
from player import Player   # import de la classe Player depuis player.py
from plane import Plane   # import de la classe Plane depuis plane.py
from sounds import SoundManager   # import de la classe SoundManager depuis sounds.py


"""CORPS DU PROGRAMME"""

# classe qui sert à gérer le jeu
class Game:
    def __init__(self):
        self.is_playing = False   # définir l'état d'activation du jeu sur False
        self.player = Player(self)   # générer notre joueur
        self.all_planes = pygame.sprite.Group()   # définir notre groupe de jet
        self.pressed = {}   # créer un dict vide pour les touches pressées
        self.all_bombs = pygame.sprite.Group()   # créer un groupe pour gérer toutes les bombes du jeu
        self.score = 0   # initialiser le score à 0
        self.police = pygame.font.Font("assets/font/font.ttf", 25)   # définir la police pour le score
        self.sound_manager = SoundManager()   # activer le sound manager

    # fonction de démarrage
    def start(self):
        self.is_playing = True   # mettre l'état d'activation sur True
        self.spawn_plane()   # faire spawn un avion
        self.spawn_plane()   # faire spawn un second avion

    # fonction de game over
    def game_over(self):
        screen = pygame.display.set_mode((1280, 667))   # définir l'écran
        game_over_image = pygame.image.load("assets/game_over.png")   # charger l'image
        game_over_image = pygame.transform.scale(game_over_image, (screen.get_width(), screen.get_height()))   # transformer l'image pour qu'elle ait la taille de l'écran
        start_time = pygame.time.get_ticks()   # lancer le chrono
        while pygame.time.get_ticks() - start_time < 5000:  # attendre 5000 millisecondes = 5 secondes
            screen.blit(game_over_image, (0, 0))   # afficher l'image
            score_text = self.police.render(f"Score : {self.score}", 1, (0, 0, 0))   # définir le texte de score
            screen.blit(score_text, (20, 20))   # afficher le score
            pygame.display.flip()   # mettre à jour l'écran
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   # quitter
                    exit()
        self.all_planes = pygame.sprite.Group()   # réinitialiser les avions
        self.all_bombs = pygame.sprite.Group()   # réinitialiser les bombes
        self.player.health = self.player.max_health   # remettre la vie au max
        self.is_playing = False   # mettre à jour l'état d'activation sur False
        self.score = 0   # mettre le score à 0

    # fonction de mise à jour
    def update(self, screen):
        score_text = self.police.render(f"Score : {self.score}", 1, (0, 0, 0))   # définir le texte pour le score
        screen.blit(score_text, (20, 20))   # afficher le score
        screen.blit(self.player.image, (200, 420))   # appliquer l'image du bateau
        for missile in self.player.all_missiles:   # récupérer les projectiles du joueur
            missile.move()   # bouger les missiles
        for plane in self.all_planes:   # récupérer les avions
            plane.forward()   # faire avancer les avions
            for missile in self.player.all_missiles:   # boucler pour chaque missile actif
                if pygame.sprite.collide_rect(missile, plane):   # vérifier la collision entre les missiles et les avions
                    self.sound_manager.play('explosion')   # jouer le son d'explosion
                    plane.respawn()   # appeler la fonction respawn de l'avion
                    missile.remove()   # supprimer le missile
        self.player.all_missiles.draw(screen)    # appliquer l'ensemble des images du groupe de missiles sur l'écran
        self.all_planes.draw(screen)   # appliquer l'ensemble des images du groupe de jets sur l'écran
        for bomb in self.all_bombs:   # boucler pour chaque bombe active
            screen.blit(bomb.image, (300, bomb.rect.y))   # afficher la bombe
            bomb.rect.y += bomb.speed   # déplacer la bombe vers le bas
            if bomb.rect.y >= screen.get_height() // 1.75:   # vérifier si la bombe a atteint une certaine position (juste au-dessus du bateau)
                bomb.kill()   # supprimer la bombe
                self.player.damage()   # infliger des dégats au joueur
                pygame.display.flip()   # mettre à jour l'écran

    # fonction de gestion des collisions
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)   # vérifier les collisions

    # fonction de spawn des jets
    def spawn_plane(self):
        plane = Plane(self)   # passer la référence au jeu lors de la création de l'instance de Plane
        self.all_planes.add(plane)   # ajouter l'avion au groupe d'avions