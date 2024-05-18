"""
Programme python principal
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""

"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import platform  # import de la librairie platform pour détecter le système d'exploitation
import os  # import de la librairie os pour influer sur le système d'exploitation
import pygame  # import de la librairie pygame pour gérer le jeu
from game import Game  # import de la classe Game depuis game.py
import time  # import de la librairie time pour le gestion du temps
from config import missile_fire_rate  # import du taux de tir de missile depuis config.py

"""CORPS DU PROGRAMME PRINCIPAL"""

# initialiser pygame
pygame.init()

# gérer les problèmes causés sur le système d'exploitation MacOs
if platform.system() == 'Darwin':  # vérifier si le système est un MacOs
    f = open("/dev/null", "w")
    os.dup2(f.fileno(), 2)
    f.close()

# générer la fenêtre du jeu
pygame.display.set_caption("Airstrike Assault")  # attribuer un nom à la fenêtre
screen = pygame.display.set_mode((1280, 667))  # attribuer une taille à la fenêtre (en pixels)
pygame.display.set_icon(pygame.image.load('assets/jet.png'))  # attribuer un logo à la fenêtre

# importer l'arrière-plan du jeu
background = pygame.image.load("assets/background2.png")  # affecter l'image de l'arrière-plan

# charger la bannière et le bouton de jeu
banner = pygame.image.load("assets/homescreen.png")
banner = pygame.transform.scale(banner, (1280, 667))

play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (280, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = 140
play_button_rect.y = 530

# charger le jeu
game = Game()  # appel de la classe Game pour charger le jeu
running = True  # définition de la variable d'exécution sur True

# Variables pour le contrôle du délai entre les tirs de missiles
last_missile_time = time.time()

# initialiser l'horloge pour contrôler le framerate
clock = pygame.time.Clock()

# tant que le programme s'exécute
while running:
    # appliquer l'arrière-plan du jeu
    screen.blit(background, (0, 0))

    if game.is_playing:
        game.update(screen)
    else:
        # ajouter homescreen
        screen.blit(banner, (0, 0))
        screen.blit(play_button, play_button_rect)

    # mise à jour de l'écran
    pygame.display.flip()

    # contrôle du framerate
    clock.tick(60)

    # si l'utilisateur ferme la fenêtre
    for element in pygame.event.get():
        if element.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif element.type == pygame.KEYDOWN:
            game.pressed[element.key] = True

            # détecter si la touche espace est pressée pour lancer notre projectile
            if element.key == pygame.K_SPACE:
                current_time = time.time()
                if current_time - last_missile_time >= missile_fire_rate:
                    game.player.launch_missile()  # appel de la fonction de lancement du missile
                    last_missile_time = current_time  # maj du temps du dernier lancement de missile

        elif element.type == pygame.KEYUP:
            game.pressed[element.key] = False

        elif element.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(element.pos):
                # lancer le jeu
                game.is_playing = True
