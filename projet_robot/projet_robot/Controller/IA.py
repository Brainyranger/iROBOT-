import time
import math
from threading import Thread
from projet_robot.Simulation.Robot import Robot
from projet_robot.Controller.Proxy_IA import largeur_robot,Proxy_simulation as proxy_simul


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

        self.robot = proxy_simul(robot)
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
        self.avancer(dt)
        self.distance_parcouru += proxy_simul.get_distance_parcourue(self,dt)
        print(self.distance_parcouru)
         	
        	
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

    def avancer(self,dt):
        self.robot.set_motor_dps(self.vitesse,self.vitesse)


class Tourner:

    def __init__(self,angle,dps,robot,str):
        """ Constructeur de notre classe Tourner 
        initialisation de la vitesse de nos roues
        initialisation de l'angle qu'on doit parcourir 
        initialisation de la distance à parcourir en degré/s pour parcourir l'angle
        initialisation de notre robot pour lequel on applique la comande"""

        self.robot = proxy_simul(robot)
        self.angle = angle
        self.dps = dps
        self.angle_parcouru = 0
        self.status = True
        self.str = str

        
    def update(self,dt):
        """ Fais la mise à jour de notre commande """

        	
        	
        if self.stop():
            self.robot.set_motor_dps(0,0)
            self.status = False
            return
        
        self.angle_parcouru += self.dps*dt/2*math.pi
        self.tourner(self.dps,dt,self.str)
        print("j'ai fini de parcourir "+str(self.angle_parcouru)+" degré")
       
	
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.angle_parcouru = 0
        self.status = True

    def stop(self):
        """ Arrête la commande en cours """

        return self.angle_parcouru > self.angle
    
    def tourner(self,dps,dt,str):
        vg = proxy_simul.vitesse_rotation_gauche(self,dps,self.angle)
        vd = proxy_simul.vitesse_rotation_droite(self,dps,self.angle)
        self.robot.set_motor_dps(vg,-vd)     
    

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

class IA_conditionnelle:
    
    def __init__(self,command1,command2,condition):
        self.cmd_1 = command1
        self.cmd_2 = command2
        self.condition = condition
        self.status = True
        
        
    def update(self,dt):
           
        if self.stop():
            return
            
        if not self.condition.detection_obstacle():
             self.cmd_1.update(dt)
        else:
             self.cmd_2.update(dt)
           
        
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.status = True
        self.cmd_1.start()
        self.cmd_2.start()  
        self.condition = self.condition.detection_obstacle()
        
    def stop(self):
        """ Arrête la commande en cours """
        
        return self.condition.detection_collision() or self.condition.detection_collision_bord_map_robot()
    

