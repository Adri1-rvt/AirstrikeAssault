"""
Programme python principal
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT,                                                         vbb                        <p^moipûojmkln b;,nvgfkr'"eé!Adrien RIVET
Version : 1.1
"""

import os
import pygame
from game import Game
pygame.init()

#Gestion Probléme MacOs
f = open("/dev/null", "w")
os.dup2(f.fileno(), 2)
f.close()


# générer la fenêtre du jeu
pygame.display.set_caption("Airstrike Assault") # à faire : rajouter icone en 2nd paramètre
screen = pygame.display.set_mode((1280, 667)) # définition de la taille de la fenetre (en pixels)

# importer l'arrière plan du jeu
background = pygame.image.load("assets/background.png")

# charger le jeu
game = Game()

running = True

# boucle tant que le programme s'exécute
while running :
    # appliquer l'arrière plan du jeu
    screen.blit(background, (0, 0))

    # appliqer l'image du joueur
    screen.blit(game.player.image, (200, 360))

    # récupérer les projectiless du joueur
    for missile in game.player.all_missiles :
        missile.move()

    # appliquer l'enesemble des images du groupe de missiles
    game.player.all_missiles.draw(screen)

    # mettre à jour l'écran
    pygame.display.flip()

    # si l'utiisateur ferme la fenêtre
    for element in pygame.event.get():
        if element.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif element.type == pygame.KEYDOWN :
            game.pressed[element.key] = True

            # détecter si la touche espace est enclenchée pour lancer notre projectile
            if element.key == pygame.K_SPACE :
                game.player.lauch_missile()