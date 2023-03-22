import time
import math
from threading import Thread
from projet_robot.Simulation.Robot import Robot
from projet_robot.Controller.Toolbox_IA import largeur_robot,Decorator,Avancer_Decorator as forward, Tourner_Decorator as turn


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
        self.status = False

    def update(self,dt) :
        """ Fais la mise à jour de notre déplacement en ligne droite """
	
        
        if self.stop():
        	self.robot.set_motor_dps(0,0)
        	self.status = False
        	return
        
        self.avancer(self.distance,dt)
        self.distance_parcouru += (self.vitesse*dt) 
        
        	
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.distance_degre = forward.getdegre_rotation(self,self.distance)
        self.distance_parcouru = 0
        self.status = True
        

    def stop(self):
        """ Arret de la commande en cours"""
        return self.distance_parcouru >= self.distance
  
        
    def	avancer(self,distance,dt):
        motor_left = self.distance_degre*dt
        motor_right = self.distance_degre*dt
        self.robot.set_motor_dps(motor_left,motor_right)
        
class Tourner:

    def __init__(self,vitesse,angle,robot):
        """ Constructeur de notre classe Tourner 
        initialisation de la vitesse de nos roues
        initialisation de l'angle qu'on doit parcourir 
        initialisation de la distance à parcourir en degré/s pour parcourir l'angle
        initialisation de notre robot pour lequel on applique la comande"""

        self.robot = turn(robot)
        self.vitesse = vitesse*3800
        self.angle = angle 
        
    def update(self,dt):
        """ Fais la mise à jour de notre commande """

        	
        	
        if self.stop():
        	self.robot.set_motor_dps(0,0)
        	self.status = False
        	return
        self.tourner_gauche(dt)
        self.angle_parcouru += self.vitesse*dt
        
        
        print("j'ai fini de parcourir "+str(self.angle_parcouru)+"degrés")
       
	
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.angle_parcouru = 0
        self.vitesse_reel = (self.vitesse/3800)*100
        self.distance_degre = turn.getdegre_rotation(self)
        self.status = True

    def stop(self):
        """ Arrête la commande en cours """

        return self.angle_parcouru > self.distance_degre
       
    def tourner_gauche(self,dt):
        motor_left = self.distance_degre*(1+(self.angle/90))*dt*self.vitesse_reel
        motor_right= self.distance_degre*(1-(self.angle/90))*dt*self.vitesse_reel
        self.robot.set_motor_dps(motor_left,motor_right)
        print(self.distance_degre)
        
    def tourner_droit(self,dt):
        motor_left = self.distance_degre*(1-(self.angle/90))*dt*self.vitesse_reel
        motor_right= self.distance_degre*(1+(self.angle/90))*dt*self.vitesse_reel
        self.robot.set_motor_dps(motor_left,motor_right)
              
