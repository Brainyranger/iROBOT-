import time
import math
import random
from threading import Thread
from projet_robot.Controller.IA import IA
from projet_robot.Controller.Toolbox_IA import largeur_robot,portee_senseur
from projet_robot.Simulation.Robot import Robot
from projet_robot.Simulation.Obstacle import Obstacle,Gemme
from projet_robot.Simulation.Senseur import Senseur,Senseur_gemme
from projet_robot.Affichage.Simulation_pygame import Simulation_pygame

class Environnement(Thread):
    
    def __init__(self,bord_map_x,bord_map_y)-> None:
        """ Initialise les éléments de notre simulation"""
        super(Environnement,self).__init__()
        self.bord_map_x = bord_map_x
        self.bord_map_y = bord_map_y
        self.running = True
        self.robot = Robot(30,300,0)
        self.senseur = Senseur(portee_senseur) 
        self.list_obs_mobiles = self.generer_obstacles(2,0.01)
        self.list_obs_immobiles = self.generer_obstacles(2,0)
        self.list_obs = self.list_obs_mobiles + self.list_obs_immobiles
        self.list_gemme = self.generer_gemme(10,10)
        self.senseur_gemme = Senseur_gemme(30)
        
	
	
    def detection_collision_bord_map_robot(self):
        """détection des collisions"""
        #Détection des bords de map
        if self.robot.x >= self.bord_map_x or self.robot.x <= 0 or self.robot.y >= self.bord_map_y or self.robot.y <= 0 :
                print("COLLISION MUR")
                self.robot.move_angle(180,"gauche")
                return True
    
    def detection_collision_bord_map_obstacle(self):
        """détection des collisions"""
        for k in range(0,len(self.list_obs_mobiles)):
            if self.list_obs_mobiles[k][0] >= self.bord_map_x-self.list_obs_mobiles[k][2] or self.list_obs_mobiles[k][0] <= 0 or self.list_obs_mobiles[k][1] >= self.bord_map_y-self.list_obs_mobiles[k][3] or self.list_obs_mobiles[k][1] <= 0:
                self.list_obs_mobiles[k][4] = - self.list_obs_mobiles[k][4]
                print("OBSTACLE REBONDIT SUR LE MUR")
    
    
    def detection_obstacle(self):
        """détection des collisions"""
        #Détection par le senseur
        self.list_obs = self.list_obs_mobiles + self.list_obs_immobiles
        for i in range(0,len(self.list_obs)):
            dist_robot_obstacle = self.senseur.get_distance(self.robot,self.list_obs[i][0],self.list_obs[i][1],self.list_obs[i][2],self.list_obs[i][3])
            if dist_robot_obstacle != False:
                print("Le senseur a détecté un obstacle à "+str(dist_robot_obstacle)+" cm")
                return True
        return False
    
    def detection_collision(self):
        """détection des collisions"""
        #Détection par la simulation
        for i in range(0,len(self.list_obs)):
            for j in range(0,largeur_robot):
                if self.robot.x+(j-largeur_robot/2)*math.cos(self.robot.angle) >= self.list_obs[i][0] and self.robot.y+(j-largeur_robot/2)*math.sin(self.robot.angle) >= self.list_obs[i][1] and self.robot.x+(j-largeur_robot/2)*math.cos(self.robot.angle) <= (self.list_obs[i][0]+self.list_obs[i][2]) and self.robot.y+(j-largeur_robot/2)*math.sin(self.robot.angle) <= (self.list_obs[i][1]+self.list_obs[i][3]):
                    print("COLLISION")
                    return True
            
        return False 

    def generer_obstacles(self,nb_obs,speed):
        """place nb_obs obstacles dans l'environnemnt """
        lr = [] 
        for i in range(0,nb_obs):
            taille_obs_x = random.uniform(20,25)
            taille_obs_y = random.uniform(20,25)
            x = random.uniform(taille_obs_x,self.bord_map_x-taille_obs_x)
            y = random.uniform(taille_obs_y,self.bord_map_y-taille_obs_y)
            obs = Obstacle(x,y,taille_obs_x,taille_obs_y,speed)
            lr.append([obs.x,obs.y,obs.taille_x,obs.taille_y,obs.vitesse,obs.angle])        
        return lr


    
    def move_obstacles(self,dt):
        """ Déplace les obstacles mobiles """
        for i in range (0,len(self.list_obs_mobiles)):
           Obstacle.move(self,self.list_obs_mobiles[i],dt)
    
    
    def generer_gemme(self,nb,rayon):
        lr = []
        for i in range(0,nb):
            x = random.uniform(rayon,self.bord_map_x-rayon)
            y = random.uniform(rayon,self.bord_map_y-rayon)
            gemme = Gemme(x,y,rayon)
            lr.append([gemme.x,gemme.y,gemme.rayon])
        return lr
            
        
    def detection_gemme(self):
        """détection des gemme"""
        #Détection par le senseur
        for i in range(0,len(self.list_gemme)):
            dist_robot_gemme = self.senseur_gemme.get_distance(self.robot,self.list_gemme[i][0],self.list_gemme[i][1],self.list_gemme[i][2])
            if dist_robot_gemme != False:
                print("Le senseur a détecté un gemme à "+str(dist_robot_gemme)+" cm")
                return True
             
        return False
    
    def detection_collision_gemme(self):
        for i in range(0,len(self.list_gemme)):
            for j in range(0,largeur_robot):
                if self.robot.x+(j-largeur_robot/2)*math.cos(self.robot.angle) >= self.list_gemme[i][0] and self.robot.y+(j-largeur_robot/2)*math.sin(self.robot.angle) >= self.list_gemme[i][1] and self.robot.x+(j-largeur_robot/2)*math.cos(self.robot.angle) <= (self.list_gemme[i][0]+self.list_gemme[i][2]) and self.robot.y+(j-largeur_robot/2)*math.sin(self.robot.angle) <= (self.list_gemme[i][1]+self.list_gemme[i][2]):
                    print("COLLISION")
                    return True
            
        return False 
         
    def update(self,dt):
        """ fais la mise à jour de notre simulation """
        self.move_obstacles(dt)
        self.robot.move(dt)
        self.detection_collision()
        self.detection_obstacle()
        self.detection_collision_bord_map_robot()
        self.detection_collision_bord_map_obstacle()
        self.detection_gemme()
        self.detection_collision_gemme()