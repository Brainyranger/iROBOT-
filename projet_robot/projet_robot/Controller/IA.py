import time
import math
from threading import Thread
from projet_robot.Simulation.Robot import Robot
from projet_robot.Controller.Toolbox_IA import Constante,Decorator,Avancer_Decorator as forward, Tourner_Decorator as turn


class IA(Thread):

    def __init__(self,ia_command):
        """ constructeur de notre classe IA
            initialisation de notre liste de commandes
            initialisation de l'état de notre commande courante"""


        super(IA,self).__init__()
        self.status = True
        self.ia_command = ia_command
        self.curr_command = 0
        
    def update(self,dt):
        """ Parcoure notre liste de commandes et éxécute commande par commande """

        if len(self.ia_command) == 0:
            self.status = False
            return
            
        if self.stop():
            self.status = False
            return
            
        if self.curr_command < len(self.ia_command) and self.ia_command[self.curr_command].stop():
            self.curr_command += 1
            self.ia_command[self.curr_command].start()
        
        self.ia_command[self.curr_command].update(dt)       

    def ajout_commandes(self,command):
        """ Ajout d'une commande à la liste de commandes """

        self.ia_command.append(command)
        
    def stop(self):
        """ Arret de l'IA """
        return self.curr_command == len(self.ia_command)-1 and self.ia_command[self.curr_command].stop()
        
        
    def getStatus(self):
        """ Renvoie l'état de l'IA """

        return self.status

    def	select_commandes(self,indice):
        """ selectionne par indice notre commande """

        if indice < 0 or indice > len(self.ia_command):
    	    return
        return self.ia_command[indice]



class Avancer:

    def __init__(self,vitesse,distance,robot):
        """ constructeur de notre classe Avancer
        initialisation de la vitesse de nos roues 
        initialisation de la distance à parcourir
        initialisation de notre robot pour lequel on applique la comande"""

        self.robot = forward(robot)
        self.vitesse = vitesse*3800
        self.distance = distance
        self.distance_parcouru = 0
        self.status = False

    def update(self,dt) :
        """ Fais la mise à jour de notre déplacement en ligne droite """
	
        
        if self.stop():
        	self.robot.set_motor_dps(0,0)
        	self.status = False
        	return
        
        forward.avancer(self,self.vitesse,dt)
        self.distance_parcouru += forward.get_distance_parcourue(self,dt)
        print("j'ai fini de parcourir "+str(self.distance_parcouru)+" cm")
         	
        	
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.distance_parcouru = 0
        self.status = True

    def stop(self):
        """ Arret de la commande en cours"""
         return self.distance_parcouru >= self.distance:


class Tourner:

    def __init__(self,vitesse,angle,dps,robot):
        """ Constructeur de notre classe Tourner 
        initialisation de la vitesse de nos roues
        initialisation de l'angle qu'on doit parcourir 
        initialisation de la distance à parcourir en degré/s pour parcourir l'angle
        initialisation de notre robot pour lequel on applique la comande"""

        self.robot = turn(robot)
        self.vitesse = vitesse*3800 
        self.angle = angle
        self.dps = dps
        self.angle_parcouru = 0
        self.status = True
        self.rayon = (60/math.tan(self.angle)) # rayon de la courbure 
        
    def update(self,dt):
        """ Fais la mise à jour de notre commande """

        	
        	
        if self.stop():
        	self.robot.set_motor_dps(0,0)
        	self.status = False
        	print("j'ai fini de parcourir "+str(self.angle_parcouru)+" degrés")
        	return
        self.angle_parcouru += self.dps*dt
        #self.angle_parcouru += turn.dist_turn(self,self.vitesse,self.angle,dt)
        print(self.angle_parcouru)
        turn.tourner(self,self.vitesse,self.dps,dt)
        #turn.tourner2(self,(self.vitesse*0.1),self.angle,self.dps,dt)
        print("j'ai fini de parcourir "+str(self.angle_parcouru)+" degrés")
       
	
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.angle_parcouru = 0
        self.status = True

    def stop(self):
        """ Arrête la commande en cours """

        return self.angle_parcouru >= self.angle:
        #return self.angle_parcouru > abs((math.pi * self.rayon)/2)*1.12
              

