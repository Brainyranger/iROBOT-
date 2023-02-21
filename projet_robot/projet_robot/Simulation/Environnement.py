import time
import math
from projet_robot.Controller.IA import IA,IA_avancer
from projet_robot.Simulation.Robot import Robot
from projet_robot.Simulation.Obstacle import Obstacle
from projet_robot.Simulation.Senseur import Senseur
from projet_robot.Simulation.Simulation_pygame import Simulation_pygame

class Environnement:
    
    def __init__(self,bord_map_x,bord_map_y)-> None:
        """ Initialise les éléments de notre simulation"""
        self.bord_map_x = bord_map_x
        self.bord_map_y = bord_map_y
        self.simul_pygame = Simulation_pygame(bord_map_x,bord_map_y)
        self.running = True
        self.robot = Robot(50,300,0)
        self.obstacle1 = Obstacle(200,300,"Obs_1",20,20)
        self.obstacle2 = Obstacle(100,80,"Obs_2",20,20)
        self.obstacle3 = Obstacle(400,200,"Obs_3",20,20)
        self.list_obs = [[self.obstacle1.x,self.obstacle1.y,self.obstacle1.taille_x,self.obstacle1.taille_y,self.obstacle1.nom],[self.obstacle2.x,self.obstacle2.y,self.obstacle2.taille_x,self.obstacle2.taille_y,self.obstacle2.nom],[self.obstacle3.x,self.obstacle3.y,self.obstacle3.taille_x,self.obstacle3.taille_y,self.obstacle3.nom]]
        self.senseur = Senseur(10)
        #self.IA = IA_avancer(self.IA,0.05,10,self.robot)
        self.dt=0
        self.temps=time.time() 
        
    def detection_collision(self):
        """détection des collisions"""
        for i in range(0,len(self.list_obs)):	
            if (self.senseur.get_distance(self.robot,self.list_obs[i][0],self.list_obs[i][1],self.list_obs[i][2],self.list_obs[i][3])) == 0:
                print("Le robot se trouve à "+str((int)(self.senseur.get_distance(self.robot,self.list_obs[i][0],self.list_obs[i][1],self.list_obs[i][2],self.list_obs[i][3])))+" cm de "+self.list_obs[i][4])
                print("COLLISION")
            elif (self.senseur.get_distance(self.robot,self.list_obs[i][0],self.list_obs[i][1],self.list_obs[i][2],self.list_obs[i][3])) == "Rien":
                print("Le senseur ne détecte pas d'obstacles")
            else:
                print("Le robot se trouve à "+str((int)(self.senseur.get_distance(self.robot,self.list_obs[i][0],self.list_obs[i][1],self.list_obs[i][2],self.list_obs[i][3])))+" cm de "+self.list_obs[i][4])
    		    

          
          
    def update(self):
        """ fais la mise à jour de notre simulation """
        self.dt = (time.time()-self.temps)
        self.temps=time.time()
        self.robot.move(self.dt)
        #self.IA.IA_avancer.run(self.robot,0.05,self.dt)
        self.detection_collision()