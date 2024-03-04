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


"""CORPS DU PROGRAMME PRINCIPAL"""

# initialiser pygame
pygame.init()

# géré les problémes causées sur le système d'exploitation MacOs
if platform.system() == 'Darwin': # vérifier si le système est un MacOs
    f = open("/dev/null", "w")
    os.dup2(f.fileno(), 2)
    f.close()

# générer la fenêtre du jeu
pygame.display.set_caption("Airstrike Assault") # attribuer un nom à la fenêtre
screen = pygame.display.set_mode((1280, 667)) # attribuer une taille à la fenetre (en pixels)
pygame.display.set_icon(pygame.image.load('assets/jet.png')) # attribuer un logo à la fenêtre

# importer l'arrière plan du jeu
background = pygame.image.load("assets/background.png") # affection l'image de l'arrière plan

# charger le jeu
game = Game() # appel de la classe Game pour charger le jeu
running = True # définition de la variable d'exécution sur 1

# tant que le programme s'exécute
while running :
    # appliquer l'arrière plan du jeu
    screen.blit(background, (0, 0))

    # appliqer l'image du bateau
    screen.blit(game.player.image, (200, 360))

    # récupérer les projectiless du joueur
    for missile in game.player.all_missiles :
        missile.move()

    # récupérer les avions
    for plane in game.all_planes:
        plane.forward()

    # appliquer l'ensemble des images du groupe de missiles
    game.player.all_missiles.draw(screen)

    # appliquer l'ensemble des images du groupe de jets
    game.all_planes.draw(screen)

    # maj de l'écran
    pygame.display.flip()

    # si l'utiisateur ferme la fenêtre
    for element in pygame.event.get():
        if element.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif element.type == pygame.KEYDOWN :
            game.pressed[element.key] = True

            # détecter si la touche espace est pressée pour lancer notre projectile
            if element.key == pygame.K_SPACE :
                game.player.lauch_missile() # appel de la fonction de lancement du missile
