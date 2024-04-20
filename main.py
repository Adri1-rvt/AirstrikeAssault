"""
Programme python principal
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""


"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import platform # import de la librairie platform pour détecter le système d'exploitation
import os # import de la librairie os pour influer sur le système d'exploitation
import pygame # import de la librairie pygame pour gérer le jeu
from game import Game # import de la classe Game depuis game.py
import time # import de la librairie time pour le gestion du temps


"""CORPS DU PROGRAMME PRINCIPAL"""

# initialiser pygame
pygame.init()

# gérer les problémes causées sur le système d'exploitation MacOs
if platform.system() == 'Darwin': # vérifier si le système est un MacOs
    f = open("/dev/null", "w")
    os.dup2(f.fileno(), 2)
    f.close()

# générer la fenêtre du jeu
pygame.display.set_caption("Airstrike Assault") # attribuer un nom à la fenêtre
screen = pygame.display.set_mode((1280, 667)) # attribuer une taille à la fenetre (en pixels)
pygame.display.set_icon(pygame.image.load('assets/jet.png')) # attribuer un logo à la fenêtre

# importer l'arrière plan du jeu
background = pygame.image.load("assets/background2.png") # affection l'image de l'arrière plan

# charger le jeu
game = Game() # appel de la classe Game pour charger le jeu
running = True # définition de la variable d'exécution sur 1

# Variables pour le contrôle du délai entre les tirs de missiles
last_missile_time = time.time()
missile_fire_rate = 1.0  # Délai minimum entre chaque tir de missile en secondes

# tant que le programme s'exécute
while running :
    # appliquer l'arrière plan du jeu
    screen.blit(background, (0, 0))

    # appliqer l'image du bateau
    screen.blit(game.player.image, (200, 420))

    # récupérer les projectiless du joueur
    for missile in game.player.all_missiles :
        missile.move()

    # récupérer les avions
    for plane in game.all_planes:
        plane.forward()

        # Vérifier la collision entre les missiles et les avions
        for missile in game.player.all_missiles:
            if pygame.sprite.collide_rect(missile, plane):
                missile.explode()  # Appel de la fonction d'explosion du missile
                plane.respawn()  # Appel de la fonction respawn de l'avion
                missile.remove()  # Supprimer le missile

    # appliquer l'ensemble des images du groupe de missiles
    game.player.all_missiles.draw(screen)

    # appliquer l'ensemble des images du groupe de jets
    game.all_planes.draw(screen)

    # maj de l'écran
    pygame.display.flip()

    # Dessine et déplace les bombes
    for bomb in game.all_bombs:
        screen.blit(bomb.image, (bomb.rect.x, bomb.rect.y))
        bomb.move()

    # si l'utiisateur ferme la fenêtre
    for element in pygame.event.get():
        if element.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif element.type == pygame.KEYDOWN :
            game.pressed[element.key] = True

            # détecter si la touche espace est pressée pour lancer notre projectile
            if element.key == pygame.K_SPACE:
                current_time = time.time()
                if current_time - last_missile_time >= missile_fire_rate:
                    game.player.launch_missile()  # appel de la fonction de lancement du missile
                    last_missile_time = current_time  # maj du temps du dernier lancement de missile

