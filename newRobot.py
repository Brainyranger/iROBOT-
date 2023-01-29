import pygame
import math
    
class Robot:
    
    def __init__(self,x,y,orientation,speed) -> None:
            
            self.x = x
            self.y = y
            self.h = orientation
            self.vitesse_max = speed

    def movement_avancer_x(self):
        #Tester avec une exception si la vitesse ne dépasse pas la vitesse max du robot
        self.x += (self.x * math.cos(self.h)) - (self.y * math.sin(self.h))

    def movement_arriere_x(self):
        #Tester avec une exception si la vitesse ne dépasse pas la vitesse max du robot
        self.x -= (self.x * math.cos(self.h)) - (self.y * math.sin(self.h))

    def movement_descend_y(self):
        #Tester avec une exception si la vitesse ne dépasse pas la vitesse max du robot
        self.y -= (self.x * math.sin(self.h)) + (self.y * math.cos(self.h))

    def movement_monte_y(self):
        #Tester avec une exception si la vitesse ne dépasse pas la vitesse max du robot
        self.y += (self.x * math.sin(self.h)) + (self.y * math.cos(self.h))

    def tourner_droite(self):
        self.h = -90

    def tourner_gauche(self):
        self.h = 90