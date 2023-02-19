
import time
import math
from projet_robot.Controller.IA import IA,IA_avancer
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
        self.LIST_OBS = [[self.obstacle1.POSITION_X,self.obstacle1.POSITION_Y,self.obstacle1.TAILLE_X,self.obstacle1.TAILLE_Y,self.obstacle1.NOM],[self.obstacle2.POSITION_X,self.obstacle2.POSITION_Y,self.obstacle2.TAILLE_X,self.obstacle2.TAILLE_Y,self.obstacle2.NOM],[self.obstacle3.POSITION_X,self.obstacle3.POSITION_Y,self.obstacle3.TAILLE_X,self.obstacle3.TAILLE_Y,self.obstacle3.NOM]]
        self.senseur = Senseur(10)
        #self.IA = IA_avancer(self.IA,0.05,10,self.robot)
        self.dt=0
        self.temps=time.time() 
        
    def detection_collision(self):
        """détection des collisions"""
        for i in range(0,len(self.LIST_OBS)):	
            if (self.senseur.get_distance(self.robot,self.LIST_OBS[i][0],self.LIST_OBS[i][1],self.LIST_OBS[i][2],self.LIST_OBS[i][3])) == 0:
                print("Le robot se trouve à "+str((int)(self.senseur.get_distance(self.robot,self.LIST_OBS[i][0],self.LIST_OBS[i][1],self.LIST_OBS[i][2],self.LIST_OBS[i][3])))+" cm de "+self.LIST_OBS[i][4])
                print("COLLISION")
            elif (self.senseur.get_distance(self.robot,self.LIST_OBS[i][0],self.LIST_OBS[i][1],self.LIST_OBS[i][2],self.LIST_OBS[i][3])) == "Rien":
                print("Le senseur ne détecte pas d'obstacles")
            else:
                print("Le robot se trouve à "+str((int)(self.senseur.get_distance(self.robot,self.LIST_OBS[i][0],self.LIST_OBS[i][1],self.LIST_OBS[i][2],self.LIST_OBS[i][3])))+" cm de "+self.LIST_OBS[i][4])
    		    

          
          
    def event_update(self):
        """ fais la mise à jour de notre simulation """
        self.dt = (time.time()-self.temps)
        self.temps=time.time()
        self.robot.MOVE(self.dt)
        #self.IA.IA_avancer.run(self.robot,0.05,self.dt)
        self.detection_collision()