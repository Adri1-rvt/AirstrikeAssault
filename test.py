from math import *
import pygame

class munitions:

    def __init__(self, direction,vitesse):
        """direction -> float"""
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