import time
import math
from threading import Thread
from projet_robot.Simulation.Robot import Robot
from projet_robot.Controller.Proxy import largeur_robot


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

    def __init__(self,vitesse,distance,robot_reel,robot_virtuel):
        """ constructeur de notre classe Avancer
        initialisation de la vitesse de nos roues 
        initialisation de la distance à parcourir
        initialisation de notre robot pour lequel on applique la comande"""

        self.robot_reel = robot_reel
        self.robot_virtuel = robot_virtuel
        self.vitesse = vitesse*3800
        self.distance = distance
        self.status = False

    def update(self,dt) :
        """ Fais la mise à jour de notre déplacement en ligne droite """
	
        
        if self.stop():
            self.robot_reel.set_motor_dps(0,0)
            self.status = False
            return
        self.avancer(dt)
        print(self.robot_virtuel.distance_parcourue)
         	
        	
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.robot_virtuel.reinitialiser_distance_parcourue()
        self.status = True

    def stop(self):
        """ Arret de la commande en cours"""
        return self.robot_virtuel.distance_parcourue >= self.distance

    def avancer(self,dt):
        self.robot_reel.set_motor_dps(self.vitesse,self.vitesse)


class Tourner:

    def __init__(self,angle,dps,robot_reel,robot_virtuel):
        """ Constructeur de notre classe Tourner 
        initialisation de la vitesse de nos roues
        initialisation de l'angle qu'on doit parcourir 
        initialisation de la distance à parcourir en degré/s pour parcourir l'angle
        initialisation de notre robot pour lequel on applique la comande"""

        self.robot_virtuel = robot_virtuel
        self.robot_reel = robot_reel
        self.angle = angle
        self.dps = dps
        self.status = True

        
    def update(self,dt):
        """ Fais la mise à jour de notre commande """

        	
        	
        if self.stop():
            self.robot_reel.set_motor_dps(0,0)
            self.status = False
            return
        
        self.robot_virtuel.angle_parcouru += self.dps*dt/2*math.pi
        self.tourner(self.dps,dt)
        print("j'ai fini de parcourir "+str(self.robot_virtuel.angle_parcouru)+" degré")
       
	
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.robot_virtuel.reinitialiser_angle_parcouru()
        self.status = True

    def stop(self):
        """ Arrête la commande en cours """

        return self.robot_virtuel.angle_parcouru >  abs(self.angle)
    
    def tourner(self,dps,dt):
        vg = self.robot_virtuel.vitesse_rotation_gauche(dps,self.angle)
        vd = self.robot_virtuel.vitesse_rotation_droite(dps,self.angle)
        
        if self.angle > 0:
            self.robot_reel.set_motor_dps(vg,-vd)
        else:
            self.robot_reel.set_motor_dps(-vg,vd)    
    

class IA_avance_led:
    
    def __init__(self,vitesse,robot,distance):
        self.vitesse = vitesse*3800
        self.robot = proxy_simul(robot)
        self.status = True
        self.distance_parcouru = 0
        self.distance = distance
        
    def update(self,dt):
        
        if self.stop():
            self.robot.set_motor_dps(0,0)
            self.status = False
        
        if self.distance_parcouru > self.distance/2:
            self.robot.set_led()
            time.sleep(0.1)
        
        self.avancer()   
        self.distance_parcouru += proxy_simul.get_distance_parcourue(self,dt)
        
    
         	
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.distance_parcouru = 0
        self.status = True

    def stop(self):
        """ Arret de la commande en cours"""
        return self.distance_parcouru >= self.distance
    
  
    def avancer(self):
        self.robot.set_motor_dps(self.vitesse,self.vitesse)
    

