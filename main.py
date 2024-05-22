"""
Programme python principal
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""

"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import platform   # import de la librairie platform pour détecter le système d'exploitation
import os   # import de la librairie os pour influer sur le système d'exploitation
import pygame   # import de la librairie pygame pour gérer le jeu
from game import Game   # import de la classe Game depuis game.py
import time   # import de la librairie time pour le gestion du temps
from config import missile_fire_rate   # import du taux de tir de missile depuis config.py


"""CORPS DU PROGRAMME PRINCIPAL"""

pygame.init()   # initialiser pygame

# gérer les problèmes causés sur le système d'exploitation MacOs
if platform.system() == 'Darwin':
    f = open("/dev/null", "w")
    os.dup2(f.fileno(), 2)
    f.close()

# générer la fenêtre du jeu
pygame.display.set_caption("Airstrike Assault")   # afficher le titre
screen = pygame.display.set_mode((1280, 667))   # définir une taille de fenetre précise
pygame.display.set_icon(pygame.image.load('assets/jet.png'))   # définir l'icône du jeu

# importer l'arrière-plan du jeu
background = pygame.image.load("assets/background2.png")   # affecter l'image de l'arrière-plan

# charger la bannière et le bouton de jeu
banner = pygame.image.load("assets/homescreen.png")   # charger l'image du fond
banner = pygame.transform.scale(banner, (1280, 667))   # transformer l'image du fond
play_button = pygame.image.load("assets/button.png")   # charger l'image du bouton
play_button = pygame.transform.scale(play_button, (280, 150))   # transformer l'image du bouton
play_button_rect = play_button.get_rect()   # définir la hitbox du bouton
play_button_rect.x = 140   # définir la position en x du bouton
play_button_rect.y = 530   # définir la position en y du bouton

# charger le jeu
game = Game()   # lancer game
game.sound_manager.play('game')   # lancer le bruit game
running = True   # mettre l'état d'activation à True
last_missile_time = time.time()   # définir une variable pour le contrôle du délai entre les tirs de missiles
clock = pygame.time.Clock()   # initialiser l'horloge pour contrôler le framerate

# tant que le programme s'exécute
while running:
    screen.blit(background, (0, 0))   # appliquer l'arrière-plan du jeu
    game.player.update_health_bar(screen)   # appliquer la barre de vie du joueur
    if game.is_playing:   # boucler si le jeu est lancé
        game.update(screen)   # mettre à jour l'écran
    else:
        screen.blit(banner, (0, 0))   # ajouter homescreen
        screen.blit(play_button, play_button_rect)   # placer le bouton de lancement

    pygame.display.flip()   # mettre à jour l'écran
    clock.tick(60)   # contrôler le framerate

    # si l'utilisateur ferme la fenêtre
    for element in pygame.event.get():
        if element.type == pygame.QUIT:   # si l'utilisateur ferme la fenêtre
            running = False   # mettre l'état d'activation à False
            pygame.quit()   # arrêter pygmae
        elif element.type == pygame.KEYDOWN:   # si une touche est pressé
            game.pressed[element.key] = True   # mettre l'état de pression à True

            # détecter si la touche espace est pressée pour lancer notre projectile
            if element.key == pygame.K_SPACE:
                current_time = time.time()   # sauvegarder le temps actuel

                # vérifier qu'un projectile n'a pas déjà été lancé il y a peu de temps
                if current_time - last_missile_time >= missile_fire_rate:
                    game.sound_manager.play('missile')   # lancer le son du missile
                    game.player.launch_missile()   # appeler la fonction de lancement du missile
                    last_missile_time = current_time   # maj du temps du dernier lancement de missile

        elif element.type == pygame.KEYUP:
            game.pressed[element.key] = False   # mettre l'état de pression à False

        # déterter si l'utilisateur a cliqué avec sa souris
        elif element.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(element.pos):   # si le clic est sur le bouton
                game.start()   # lancer le jeu
                game.sound_manager.play('click')   # lancer le son du click du jeu