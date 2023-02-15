
import time
import math
from newRobot import newRobot
from Obstacle import Obstacle
from Senseur import Senseur

class Simulation_finale:
    
    def __init__(self,bord_map_x,bord_map_y)-> None:
        """ initialise les éléments de notre simulation"""
        self.bord_map_x = bord_map_x
        self.bord_map_y = bord_map_y
        self.running = True
        self.robot = newRobot(50,300,0,50)
        self.obstacle1 = Obstacle(200,300,"Obs_1",20,20)
        self.obstacle2 = Obstacle(100,80,"Obs_2",20,20)
        self.obstacle3 = Obstacle(400,200,"Obs_3",20,20)
        self.list_obs = [[self.obstacle1.x,self.obstacle1.y],[self.obstacle2.x,self.obstacle2.x],[self.obstacle3.x,self.obstacle3.x]]
        self.senseur = Senseur(10)
        self.dt=0
        self.temps=time.time() 
        
    def detection_collision(self,newRobot,list_obs):
        """détection des collisions"""
        for i in range(0,len(list_obs)):
         x=list_obs[i][0] 
         y=list_obs[i][1]	
         if (int)(self.senseur.get_distance(self.robot,[x,y])) == 0:
    		    print("collision")
          
          
    def event_update(self):
        """ fais la mise à jour de notre simulation """
        self.dt = (time.time()-self.temps)
        self.temps=time.time()
        self.robot.move(self.dt)
        self.detection_collision(self.robot,self.list_obs)
