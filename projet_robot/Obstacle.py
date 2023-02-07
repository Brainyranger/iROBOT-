import pygame
import numpy as np

class Obstacle:
    #création d'obstacle
    
    def __init__(self,x,y,nom):
        """ enresgistre les coordoonnées de nos obstacles"""
        self.x=x
        self.y=y
        self.nom = nom
        self.list_obstacle = []
        self.list_obstacle.append([x,y])
        self.colour = (255,0,0)
        self.obstacle = pygame.Rect(x,y,20,20)
    #affichage d'obstacle
    
    def draw_obstacle(self,screen):
        """ dessine nos obstacles selon ses coordonnées"""
        pygame.draw.rect(screen,self.colour,self.obstacle)
        
        
    