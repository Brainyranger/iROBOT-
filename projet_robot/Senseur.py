import pygame
import time
import math
import numpy as np
from Obstacle import *
from newRobot import * 

class Senseur:

    def __init__(self,sensor_range,map):
        """ initialise notre capteur"""
        self.sensor_range = sensor_range
        self.map_width, self.map_height= pygame.display.get_surface().get_size()
        self.map = map
        self.distance = 0
        self.red = (255,0,0)
        
    def get_distance(self,distance)->float:
        """ coverti pixel en cm"""
        self.distance = distance*0.026
        return self.distance
    
    def sense_obstacles(self,newRobot,list_obs,heading):
        """ permet au senseur de detecter les obstacle et les collisions"""
        dist_min= 5 
 
        x1 = newRobot.x
        y1 = newRobot.y
        start_angle = heading - self.sensor_range[1]
        finish_angle = heading + self.sensor_range[1]
        for angle in np.linspace(start_angle,finish_angle,10,False):
            x2 = x1 + self.sensor_range[0]*math.cos(angle)
            y2 = y1 + self.sensor_range[0]*math.sin(angle)
            for i in range(0,100):
                u = 1/100
                newRobot.x = int(x2*u+x1*(1-u))
                newRobot.y = int(y2*u+y1*(1-u))
                for i in range(0,len(list_obs)):
                    
                    x=list_obs[i][0]
                    y=list_obs[i][1]
                    dist = math.sqrt(((x-newRobot.x)**2)+((y-newRobot.y)**2))
                    
                    if (int)(self.get_distance(dist)) == 0:
                        print("collision")
                        
                    if 0 < (int)(self.get_distance(dist)) < dist_min:
                        print("Obstacle à "+str((int)(self.get_distance(dist)))+" cm")
            
                    
              
        
        
