import pygame
import sys
from pygame.locals import *
import numpy as np

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
    #affichage d'obstacle
    
    def draw_obstacle(self,screen):
        """ dessine nos obstacles selon ses coordonnées"""
        obstacle = pygame.Rect(self.x,self.y,self.taille_x,self.taille_y)
        pygame.draw.rect(screen,self.colour,obstacle)
    
    
        
              