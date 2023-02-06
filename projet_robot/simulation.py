import pygame
import sys
from Obstacle import *
from newRobot import *
from Senseur import *
        
class Simulation:
    
    def __init__(self,surface_map)-> None:
        """ initialise les éléments de notre simulation"""
        self.surface_map = surface_map
        self.running = True
        self.clock = pygame.time.Clock()
        self.robot =  newRobot(0,0,0,0)
        self.robot2 = newRobot(50,300,0,0)
        self.obstacle1 = Obstacle(200,300,"Obstacle1")
        self.obstacle2 = Obstacle(100,80,"Obstacle2")
        self.obstacle3 = Obstacle(400,200,"Obstacle3")
        self.list_obs = [[200,300],[100,80],[400,200]]
        self.senseur = Senseur([200,math.radians(40)],self.surface_map)
        self.senseur_obs = self.senseur.sense_obstacles(self.robot,self.list_obs,self.robot.h)
    
            
    def event_gestion(self):
        """ gère les divers événements de notre simulation"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.robot.velocity[0] = -1
        elif keys[pygame.K_RIGHT]:
            self.robot.velocity[0] = 1 
        else:
            self.robot.velocity[0] = 0
            
        if keys[pygame.K_UP]:
            self.robot.velocity[1] = -1
        elif keys[pygame.K_DOWN]:
            self.robot.velocity[1] = 1 
        else:
            self.robot.velocity[1] = 0
                   
        
            
    def event_update(self):
        """ fais la mise à jour de notre simulation """
        self.robot.move()
        self.senseur.sense_obstacles(self.robot,self.list_obs,self.robot.h)
            
    
    def display(self):
        """ affiche notre simulation """
        self.surface_map.fill("White")
        self.robot.draw_robot(self.surface_map)
        self.robot2.draw_robot(self.surface_map)
        #draw obstacle
        self.obstacle1.draw_obstacle(self.surface_map,200,200)
        self.obstacle2.draw_obstacle(self.surface_map,100,80)
        self.obstacle3.draw_obstacle(self.surface_map,400,200)
        
        pygame.display.flip()
        

            
            