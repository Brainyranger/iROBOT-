
import time
import math
from  projet_robot.Simulation.newRobot import Robot
from  projet_robot.Simulation.Obstacle import Obstacle
from  projet_robot.Simulation.Senseur import Sensor

class Environnement:
    
    def __init__(self,bord_map_x,bord_map_y)-> None:
        """ initialise les éléments de notre simulation"""
        self.bord_map_x = bord_map_x
        self.bord_map_y = bord_map_y
        self.running = True
        self.robot = Robot(50,300,0,50)
        self.obstacle1 = Obstacle(200,300,"Obs_1",20,20)
        self.obstacle2 = Obstacle(100,80,"Obs_2",20,20)
        self.obstacle3 = Obstacle(400,200,"Obs_3",20,20)
        self.list_obs = [[self.obstacle1.x,self.obstacle1.y],[self.obstacle2.x,self.obstacle2.x],[self.obstacle3.x,self.obstacle3.x]]
        self.senseur = Sensor(10)
        self.dt=0
        self.temps=time.time() 
        
    def detection_collision(self,Robot,list_obs):
        """détection des collisions"""
        for i in range(0,len(list_obs)):
            x=list_obs[i][0] 
            y=list_obs[i][1]	
            if (self.senseur.get_distance(Robot,x,y)) == 0:
                print("Le robot se trouve à "+str((int)(self.sensor.get_distance(Robot,x,y)))+" cm de Obs_")
                print("COLLISION")
            elif (self.senseur.get_distance(Robot,x,y)) == "Rien":
                print("Le senseur ne détecte pas d'obstacles")
            else:
                print("Le robot se trouve à "+str((int)(self.sensor.get_distance(Robot,x,y)))+" cm de Obs_")
    		    

          
          
    def event_update(self):
        """ fais la mise à jour de notre simulation """
        self.dt = (time.time()-self.temps)
        self.temps=time.time()
        self.robot.move(self.dt)
        self.detection_collision(self.robot,self.list_obs)