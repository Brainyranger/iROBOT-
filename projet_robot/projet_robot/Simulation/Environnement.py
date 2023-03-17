import time
import math
import random
from threading import Thread
from projet_robot.Controller.IA import IA
from projet_robot.Controller.Toolbox_IA import Constante as const
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
        self.senseur = Senseur(const.getPorteeSenseur()) 
        self.list_obs=self.generer_obstacles(5)
        
	
    def detection_collision(self):
        """détection des collisions"""
        #Détection des bords de map
        if self.robot.x >= self.bord_map_x or self.robot.x <= 0 or self.robot.y >= self.bord_map_y or self.robot.y <= 0 :
                self.robot.move_angle(180)
        #Détection par le senseur
        for i in range(0,len(self.list_obs)):
            dist_robot_obstacle = self.senseur.get_distance(self.robot,self.list_obs[i][0],self.list_obs[i][1],self.list_obs[i][2],self.list_obs[i][3])
            if dist_robot_obstacle != False:
                print("Le senseur a détecté un obstacle à "+str(dist_robot_obstacle)+" cm")
            #Détection par la simulation
            for j in range(0,const.getLargeurRobot()):
                if self.robot.x+(j-const.getLargeurRobot()/2)*math.cos(self.robot.angle) >= self.list_obs[i][0] and self.robot.y+(j-const.getLargeurRobot()/2)*math.sin(self.robot.angle) >= self.list_obs[i][1] and self.robot.x+(j-const.getLargeurRobot()/2)*math.cos(self.robot.angle) <= (self.list_obs[i][0]+self.list_obs[i][2]) and self.robot.y+(j-const.getLargeurRobot()/2)*math.sin(self.robot.angle) <= (self.list_obs[i][1]+self.list_obs[i][3]):
                    print("COLLISION")
                    return True
        return False 

    def generer_obstacles(self,nb_obs):
        """place nb_obs obstacles dans l'environnemnt en faisant attention à ne pas
        supperposer les obstacles"""
        lr = [] 
        for i in range(0,nb_obs):
            taille_obs_x = random.randint(20,23)
            taille_obs_y = random.randint(27,30)
            x = random.randint(taille_obs_x,self.bord_map_x-taille_obs_x)
            y = random.randint(taille_obs_y,self.bord_map_y-taille_obs_y)
            obs = Obstacle(x,y,taille_obs_x,taille_obs_y)
           
            lr.append([obs.x,obs.y,obs.taille_x,obs.taille_y])        
        return lr
          
    def update(self,dt):
        """ fais la mise à jour de notre simulation """
        self.robot.move(dt)
        self.detection_collision()
