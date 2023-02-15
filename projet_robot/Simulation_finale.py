
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
        self.robot = newRobot(50,300,0,0,59,bord_map_x,bord_map_y)
        self.obstacle1 = Obstacle(200,300,"Obs_1",20,20)
        self.obstacle2 = Obstacle(100,80,"Obs_2",20,20)
        self.obstacle3 = Obstacle(400,200,"Obs_3",20,20)
        self.list_obs = [[self.obstacle1.x,self.obstacle1.y],[self.obstacle2.x,self.obstacle2.x],[self.obstacle3.x,self.obstacle3.x]]
        self.senseur = Senseur(bord_map_x,bord_map_y)
        self.dt=0
        self.temps=time.time() 
        
    def detection_obstacle(self,newRobot,list_obs):
        """détection des collisions"""
        for i in range(0,len(list_obs)):
         x=list_obs[i][0] 
         y=list_obs[i][1]
         dist = math.sqrt(((x-newRobot.x)**2)+((y-newRobot.y)**2))
    		
         if (int)(self.senseur.get_distance(dist)) == 0:
    		    print("collision")
          
          
    def event_update(self):
        """ fais la mise à jour de notre simulation """
        self.dt = (time.time()-self.temps)
        self.temps=time.time()
        self.robot.move(self.dt)
        self.senseur.sense_obstacles(self.robot,self.list_obs)
        self.detection_obstacle(self.robot,self.list_obs)
