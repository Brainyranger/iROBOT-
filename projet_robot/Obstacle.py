import pygame
from pygame.locals import *

class Obstacle:
    #création d'obstacle
    
    def __init__(self,x,y,nom,taille_x,taille_y):
        """ enresgistre les coordoonnées de nos obstacles"""
        self.x=x
        self.y=y
        self.nom = nom
        self.taille_x = taille_x
        self.taille_y = taille_y
        self.list_obstacle = []
        self.list_obstacle.append([x,y])
        self.colour = (0,0,255)
    

    
    
        
              