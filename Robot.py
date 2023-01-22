import pygame
import math
    
class Robot:
    
    def __init__(self,x,y,orientation,speed) -> None:
            
            self.x = x
            self.y = y
            self.h = orientation
            self.vitesse_max = speed
            
 
    def movement_avancer_x(self):
        self.x = self.x+self.vitesse_max
      
    def movement_arriere_x(self):
        self.x = (self.x)-(self.vitesse_max)
        
    def movement_descend_y(self):
        self.y = self.y+self.vitesse_max
        
    def movement_monte_y(self):
        self.y = (self.y)-(self.vitesse_max)
        
    def tourner_droite(self):
        self.h = -90
        
    def tourner_gauche(self):
        self.h = 90

    
