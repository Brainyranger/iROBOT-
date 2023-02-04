import pygame
import math
from Obstacle import *
from newRobot import * 

class Senseur:

    def __init__(self, sensor_range, map):
        self.sensor_range = sensor_range
        self.map_width, self.map_height= pygame.display.get_surface().get_size()
        self.map = map
        
    def get_distance(self,distance)->float:
        """ coverti pixel en cm"""
        return distance*0.026
    
    def sense_obstacles(self,newRobot,list_obs)->None:
        """ permet au senseur de detecter les obstacle """
        dist_min=200
        dist_collision = 100
        
        for i in range(0,len(list_obs)):
            for j in range(0,len(list_obs[i])-1):
                x=list_obs[i][j]
                y=list_obs[i][j+1]
            dist = math.sqrt(((x-newRobot.x)**2)+((y-newRobot.y)**2))
            if dist < dist_min:
                print("je suis devant un obstacle")
            
            if dist < dist_collision:
                print("je suis rentré en colission avec l'obstacle")
            else:
                  print("je n'ai pas encore détecter d'obstacle")
                
         
        