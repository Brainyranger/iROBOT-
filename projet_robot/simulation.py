import pygame
import sys
import time
from Obstacle import *
from newRobot import *
from Senseur import *
        
class Simulation:
    
    def __init__(self,surface_map)-> None:
        """ initialise les éléments de notre simulation"""
        self.surface_map = surface_map
        self.running = True
        self.clock = pygame.time.Clock()
        self.robot =  newRobot(0,0,0,0,50)
        self.robot2 = newRobot(50,300,0,0,50)
        self.obstacle1 = Obstacle(200,300,"Obs_1")
        self.obstacle2 = Obstacle(100,80,"Obs_2")
        self.obstacle3 = Obstacle(400,200,"Obs_3")
        self.list_obs = [[200,300],[100,80],[400,200]]
        self.senseur = Senseur(self.surface_map)
        self.dt=0
        self.temps=time.time()    

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
        self.dt = (time.time()-self.temps)
        self.temps=time.time()
        self.robot.move()
        self.robot2.move_2(self.dt)
        self.senseur.sense_obstacles(self.robot2,self.list_obs)
            
    
    def display(self):
        """ affiche notre simulation """
        #draw surface
        self.surface_map.fill("White")
        #self.robot.draw_robot(self.surface_map)
        self.robot2.draw_robot2(self.robot2.x,self.robot2.y,self.robot2.h,self.surface_map)
        #draw sensor
        self.senseur.draw_sensor(self.robot2,self.list_obs)
        #draw obstacle
        self.obstacle1.draw_obstacle(self.surface_map)
        self.obstacle2.draw_obstacle(self.surface_map)
        self.obstacle3.draw_obstacle(self.surface_map)
        
        
        pygame.display.flip()
        

            
            