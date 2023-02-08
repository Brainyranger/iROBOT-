import sys
import time
from Obstacle import *
from newRobot import *
from Senseur import *
        
class Simulation_finale:
    
    def __init__(self,bord_map_x,bord_map_y)-> None:
        """ initialise les éléments de notre simulation"""
        self.bord_map_x = bord_map_x
        self.bord_map_y = bord_map_y
        self.running = True
        self.robot =  newRobot(0,0,0,0,50,bord_map_x,bord_map_y)
        self.robot2 = newRobot(50,300,0,0,50,bord_map_x,bord_map_y)
        self.obstacle1 = Obstacle(200,300,"Obs_1",20,20)
        self.obstacle2 = Obstacle(100,80,"Obs_2",50,50)
        self.obstacle3 = Obstacle(400,200,"Obs_3",100,100)
        self.list_obs = [[self.obstacle1.x,self.obstacle1.y],[self.obstacle2.x,self.obstacle2.x],[self.obstacle3.x,self.obstacle3.x]]
        self.senseur = Senseur(bord_map_x,bord_map_y)
        self.dt=0
        self.temps=time.time() 