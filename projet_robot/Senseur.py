import pygame
import time
import math
import numpy as np
from Obstacle import *
from newRobot import * 

class Senseur:

    def __init__(self,map):
        """ initialise notre capteur"""
        self.map_width, self.map_height= pygame.display.get_surface().get_size()
        self.map = map
        self.distance = 0
        self.red = (255,0,0)
        self.green = (0,255,0)
        
    def get_distance(self,distance)->float:
        """ converti pixel en cm"""
        self.distance = distance*0.026
        return self.distance
    
    def sense_obstacles(self,newRobot,list_obs):
        """ permet au senseur de detecter les obstacle et les collisions"""
        dist_min= 10 
        
        
        for i in range(0,len(list_obs)):
                    
            x=list_obs[i][0]
            y=list_obs[i][1]
            dist = math.sqrt(((x-newRobot.x)**2)+((y-newRobot.y)**2))
                   
            if (int)(self.get_distance(dist)) == 0:
                print("collision")
                
                        
            if 0 < (int)(self.get_distance(dist)) < dist_min:
                if i == 0:
                    print("Obstacle 1 à "+str((int)(self.get_distance(dist)))+" cm")
                    
                if i == 1:
                    print("Obstacle 2 à "+str((int)(self.get_distance(dist)))+" cm")
                    
                if i == 2:
                    print("Obstacle 3 à "+str((int)(self.get_distance(dist)))+" cm")
                    
                    
                
                    
    
    
    def draw_sensor(self,NewRobot,list_obs):
        for p in list_obs:
            pygame.draw.line(self.map,self.green,p,(NewRobot.x,NewRobot.y))  
        
 
