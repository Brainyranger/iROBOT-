import pygame
import numpy as np

class Obstacle:
    #création d'obstacle
    
    def __init__(self,x,y):
        """ enresgistre les coordoonnées de nos obstacles"""
        self.x=x
        self.y=y
        self.list_obstacle = []
        self.list_obstacle.append([x,y])
        self.obstacle = pygame.image.load("/home/david/iROBOT-/projet_robot/style-realiste-bombe-noire-ronde.jpg")
     
    #affichage d'obstacle
    
    def draw_obstacle(self,screen,x,y):
        """ dessine nos obstacles selon ses coordonnées"""
        self.rect_obs = self.obstacle.get_rect(x=x,y=y)
        screen.blit(self.obstacle,self.rect_obs)
        
    