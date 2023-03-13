import time
import math
from threading import Thread
from projet_robot.Simulation.Robot import Robot
from projet_robot.Controller.Toolbox_IA import Constante,Decorator,Avancer_decorator


global WHEEL_DIAMETER 
global WHEEL_BASE_WIDTH   
WHEEL_DIAMETER = 5
WHEEL_BASE_WIDTH= 60

class IA(Thread):

    def __init__(self,ia_commande):
        """ constructeur de notre classe IA
            initialisation de notre liste de commandes
            initialisation de l'état de notre commande courante"""


        super(IA,self).__init__()
        self.status = True
        self.ia_commande = ia_commande
        
    def update(self,dt):
        """ Parcoure notre liste de commandes et éxécute commande par commande """

        if len(self.ia_commande) == 0:
            self.stop()
        else:
            for i in range(0,len(self.ia_commande)):
                if self.ia_commande[i].getStatus() == True:
                    self.ia_commande[i].update(dt)
                    return
            self.stop()
                

    def ajout_commandes(self,commande):
        """ Ajout d'une commande à la liste de commandes """

        self.ia_commande.append(commande)
        
    def stop(self):
        """ Arret de l'IA """

        self.status = False
        
    def getStatus(self):
        """ Renvoie l'état de l'IA """

        return self.status

    def	select_commandes(self,indice):
        """ selectionne par indice notre commande """

        if indice < 0 or indice > len(self.ia_commande):
    	    return
        return self.ia_commande[indice]


class Avancer:

    def __init__(self,vitesse,distance,robot):
        """ constructeur de notre classe Avancer
        initialisation de la vitesse de nos roues 
        initialisation de la distance à parcourir
        initialisation de notre robot pour lequel on applique la comande"""

        self.robot = Decorator(robot)
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
        	
        self.distance_parcouru += Avancer_deux.get_distance_parcourue(self,dt)
        Avancer_decorator.avancer(self,dt)
         	
        	
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


class Tourner:

    def __init__(self,vitesse,angle,dps,robot):
        """ Constructeur de notre classe Tourner 
        initialisation de la vitesse de nos roues
        initialisation de l'angle qu'on doit parcourir 
        initialisation de la distance à parcourir en degré/s pour parcourir l'angle
        initialisation de notre robot pour lequel on applique la comande"""

        self.robot = robot
        self.vitesse = vitesse
        self.angle = angle
        self.dps = dps
        self.angle_parcouru = 0
        self.angleInitial = self.robot.getAngleEnDegre()
        self.status = True

    def update(self,dt):
        """ Fais la mise à jour de notre commande """

        if self.angle_parcouru < self.angle:
            if self.dps == 0:
                self.stop()
            else:
                self.robot.set_motor_dps(self.vitesse,self.vitesse)
                angle = self.dps*dt
                if (angle + self.angle_parcouru) > self.angle:
                    angle = self.angleInitial+self.angle - self.robot.getAngleEnDegre()
                    self.angleInitial += self.angle
                    self.angle_parcouru = self.angle
                else :
                    self.angle_parcouru += angle
                self.robot.move_angle(angle)
                print("j'ai fini de parcourir "+str(self.angle_parcouru)+" degré")
        else:
            self.angle_parcouru = 0
            self.stop()

    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """

        self.status = True

    def stop(self):
        """ Arrête la commande en cours """

        self.status = False
        



class Square:

    def __init__(self,Robot):
        """ Constructeur de la classe Square, commande pour faire un carrée 
        initialisation du robot pour lequel on applique la commande
        initialisation de l'état de la commande 
        initialisation de la capacité d'aller tout droit 
        initilisation de la capcité de tourner à gauche
         """

        self.robot = Robot
        self.toutDroit = Avancer(0.03,6,self.robot)
        self.tournerGauche = Tourner(0,90,30,self.robot)
        self.count = 0
        self.status = True
			 
    def stop(self):
        """ Arrête la commande en cours """

        self.status = False

    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """

        self.status = True
        
    def update(self,dt):
        """ Fais la mise à jour de notre commande """

        if self.count == 8 or self.status == False:
            self.stop()
        else:
            if self.toutDroit.getStatus() == True:
                self.toutDroit.update(dt)
            else:
                if self.tournerGauche.getStatus() == True:
                    self.tournerGauche.update(dt)
                else:
                    self.count += 2
                    self.toutDroit.start()
                    self.tournerGauche.start()            


class Triangle:

    def	__init__(self,robot):
        """ Constructeur de notre classe Triangle, pour tracer un Trinagle
        initilisation du robot pour lequel on applique la commande
        initialisation de l'état de la commande 
        initialisation de la capacité d'aller tout droit 
        initilisation de la capcité de tourner à gauche
         """
         
        self.robot = robot
        self.tournerTriangle = Tourner(0,120,30,self.robot)
        self.toutDroit = Avancer(0.03,8,self.robot)
        self.count = 0
        self.status = True

    def start(self):
        """ Lance la commande """

        self.status = True
				
    def stop(self):
        """ Arrête la commande en cours """

        self.status = False

    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status
		
    def update(self,dt):
        """ Fais la mise à jour de la commande """
        
        if self.count == 6 or self.status == False:
            self.stop()
        else:
            if self.toutDroit.getStatus() == True:
                self.toutDroit.update(dt)
            else:
                if self.tournerTriangle.getStatus() == True:
                    self.tournerTriangle.update(dt)
                else:
                    self.count += 2
                    self.toutDroit.start()
                    self.tournerTriangle.start()


class Approche_Mur:

	def	__init__(self,acceleration,vitesse_freinage,pos_mur,robot):
        """ contructeur de la classe approche Mur
        initialise un robot pour lequel on applique la commande
        initialise l'environnement du robot
        initialise la vitesse des roues du robot"""

		self.robot = robot
        self.vitesse = 0
        self.vitesse_freinage = vitesse_freinage*3800
        self.acceleration = acceleration*3800
        self.pos_mur = pos_mur
        self.distance_arret = 0
        self.compteur = True
        self.status = True
		
		
	def	start(self):
        """ Lance la commande """
		self.status = True
		
	def	stop(self):
        """ Arrête de la commande en cours """
		self.status = False
		
	def getStatus(self):
        """ renvoie l'état de la commande """
        	return self.status
		
	def update(self,dt) :
        if self.compteur == True:
            v = self.vitesse
            self.distance_arret = 0
            while v > 0:
                v -= self.vitesse_freinage
                self.distance_arret += v*math.cos(self.robot.angle)*dt + v*math.sin(self.robot.angle)*dt
        if self.robot.getmovex(2*dt)+self.distance_arret < self.pos_mur:
            self.vitesse += self.acceleration
            self.robot.set_motor_dps(self.vitesse,self.vitesse)
        else:
            self.compteur = False
            print(self.distance_arret)
            if self.vitesse > 0:
                self.vitesse -= self.vitesse_freinage
                self.robot.set_motor_dps(self.vitesse,self.vitesse)
            else:
                self.robot.set_motor_dps(0,0)
                self.stop()
			