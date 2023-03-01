import time
import math
import random
from threading import Thread
from projet_robot.Controller.IA import IA
from projet_robot.Simulation.Robot import Robot
from projet_robot.Simulation.Obstacle import Obstacle
from projet_robot.Simulation.Senseur import Senseur
from projet_robot.Affichage.Simulation_pygame import Simulation_pygame

class Environnement(Thread):
    
    def __init__(self,bord_map_x,bord_map_y)-> None:
        """ Initialise les éléments de notre simulation"""
        super(Environnement,self).__init__()
        self.bord_map_x = bord_map_x
        self.bord_map_y = bord_map_y
        self.running = True
        self.robot = Robot(50,300,0)
        self.senseur = Senseur(30) 
        self.list_obs=self.generer_obstacles(5)
        
	
    def detection_collision(self):
        """détection des collisions"""
        if self.robot.x >= self.bord_map_x or self.robot.x <= 0 or self.robot.y >= self.bord_map_y or self.robot.y <= 0 :
                print(self.robot.angle)
                self.robot.angle += math.pi
                if self.robot.angle >= 2*math.pi:
                    self.robot.angle -= 2*math.pi
                print(self.robot.angle)
        for i in range(0,len(self.list_obs)):
            dist_robot_obstacle = self.senseur.get_distance(self.robot,self.list_obs[i][0],self.list_obs[i][1],self.list_obs[i][2],self.list_obs[i][3])
            if dist_robot_obstacle == 0:
                print("COLLISION")
              
            if dist_robot_obstacle == "Rien":
                print("Le senseur ne détecte pas d'obstacles")
            else:
                print("Le senseur a détecté un obstacle à "+str((int)(dist_robot_obstacle))+" cm")
 

    def generer_obstacles(self,nb_obs):
        """place nb_obs obstacles dans l'environnemnt en faisant attention à ne pas
        supperposer les obstacles ni de le poser sur le robot"""
        lr = [] 
        ens_obs = set()
        for i in range(0,nb_obs):
            taille_obs = random.randint(20,30)
            x = random.randint(taille_obs,self.bord_map_x-taille_obs)
            y = random.randint(taille_obs,self.bord_map_y-taille_obs)
            obs = Obstacle(x,y,taille_obs,taille_obs)
            if obs.x not in ens_obs and obs.y not in ens_obs and obs.x+taille_obs//2 not in ens_obs and obs.y+taille_obs//2 not in ens_obs:
            	ens_obs.add(obs.x)
            	ens_obs.add(obs.y)
            	lr.append([obs.x,obs.y,obs.taille_x,obs.taille_y])        
        return lr
          
    def update(self,dt):
        """ fais la mise à jour de notre simulation """
        self.robot.move(dt)
        self.detection_collision()
