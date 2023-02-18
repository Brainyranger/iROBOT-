
import time
import math
from  projet_robot.Simulation.Robot import Robot
from  projet_robot.Simulation.Obstacle import Obstacle
from  projet_robot.Simulation.Senseur import Senseur

class Environnement:
    
    def __init__(self,BORD_MAP_X,BORD_MAP_Y)-> None:
        """ Initialise les éléments de notre simulation"""
        self.BORD_MAP_X = BORD_MAP_X
        self.BORD_MAP_Y = BORD_MAP_Y
        self.running = True
        self.robot = Robot(50,300,0)
        self.obstacle1 = Obstacle(200,300,"Obs_1",20,20)
        self.obstacle2 = Obstacle(100,80,"Obs_2",20,20)
        self.obstacle3 = Obstacle(400,200,"Obs_3",20,20)
        self.LIST_OBS = [[self.obstacle1.x,self.obstacle1.y],[self.obstacle2.x,self.obstacle2.x],[self.obstacle3.x,self.obstacle3.x]]
        self.senseur = Senseur(10)
        self.dt=0
        self.temps=time.time() 
        
    def detection_collision(self):
        """détection des collisions"""
        for i in range(0,len(self.LIST_OBS)):
            x=self.LIST_OBS[i][0] 
            y=self.LIST_OBS[i][1]	
            if (self.senseur.get_distance(self.robot,x,y)) == 0:
                print("Le robot se trouve à "+str((int)(self.sensor.get_distance(self.robot,x,y)))+" cm de Obs_")
                print("COLLISION")
            elif (self.senseur.get_distance(self.robot,x,y)) == "Rien":
                print("Le senseur ne détecte pas d'obstacles")
            else:
                print("Le robot se trouve à "+str((int)(self.sensor.get_distance(self.robot,x,y)))+" cm de Obs_")
    		    

          
          
    def event_update(self):
        """ fais la mise à jour de notre simulation """
        self.dt = (time.time()-self.temps)
        self.temps=time.time()
        self.robot.MOVE(self.dt)
        self.detection_collision()