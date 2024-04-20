from math import *
import pygame

class munitions:

    def __init__(self, direction,vitesse):
        self.vitesse = vitesse
        self.direction = direction * (pi / 180)
        self.temp = 0
        self.rotation = 0
        self.x = None
        self.y = None

    def next_spot(self, coordinate):
        g = 9.81
        Px = self.vitesse * cos(self.direction) * self.temp
        Py = -(1 / 2) * g * (self.temp ** 2) + self.vitesse * sin(self.direction) * self.temp
        return coordinate[0] + Px, coordinate[1] - Py

    def fire(self, coordinate):
        Px, Py = self.next_spot(coordinate)
        self.temp += 0.01
        self.x = Px
        self.y = Py
        return Px, Py

    def rotate(self):
        self.rotation -= 1



import pygame
import sys
import math

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Missile Trajectory")

# Couleurs
white = (255, 255, 255)
red = (255, 0, 0)

# Paramètres de la trajectoire parabolique
initial_position = (100, height - 50)  # Position initiale du missile
initial_speed = 20  # Vitesse initiale du missile
angle = 45  # Angle de lancement
gravity = 0.5  # Gravité

# Convertir l'angle en radians
angle_radians = math.radians(angle)

# Calculer les composantes de la vitesse initiale
initial_velocity_x = initial_speed * math.cos(angle_radians)
initial_velocity_y = -initial_speed * math.sin(angle_radians)

# Variables de la trajectoire
time = 0
time_increment = 0.1
missile_position = list(initial_position)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculer la position du missile en fonction du temps
    missile_position[0] = initial_position[0] + initial_velocity_x * time
    missile_position[1] = initial_position[1] + \
        (initial_velocity_y * time + 0.5 * gravity * time**2)

    # Effacer l'écran
    screen.fill(white)

    # Dessiner le missile
    pygame.draw.circle(screen, red, (int(missile_position[0]), int(missile_position[1])), 10)

    # Dessiner une ligne du point de lancement au point actuel du missile
    pygame.draw.line(screen, red, initial_position, missile_position, 2)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Mettre à jour le temps
    time += time_increment

    # Réguler la vitesse de la boucle
    pygame.time.Clock().tick(30)