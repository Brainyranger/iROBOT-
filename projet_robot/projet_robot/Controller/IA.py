import time
import math
from threading import Thread
from projet_robot.Simulation.Robot import Robot

global WHEEL_DIAMETER 
global WHEEL_BASE_WIDTH   
WHEEL_DIAMETER = 5
WHEEL_BASE_WIDTH= 40

class IA(Thread):

    def __init__(self,IA_commande):
        """ constructeur de notre classe IA
            initialisation de notre liste de commandes
            initialisation de l'état de notre commande courante"""


        super(IA,self).__init__()
        self.Status = True
        self.IA_commande = [IA_commande]
        
    def step(self,dt):
        """ Parcoure notre liste de commandes et éxécute commande par commande """

        if self.IA_commande == []:
            self.stop()
        else:
            for i in range(0,len(self.IA_commande)):
                if self.IA_commande[i].getStatus() == True:
                    self.IA_commande[i].update(dt)
                    return
            self.stop()
                

    def ajout_commandes(self,commande):
        """ Ajout d'une commande à la liste de commandes """

        self.IA_commande.append(commande)
        
    def stop(self):
        """ Arret de l'IA """

        self.Status = False
        
    def getStatus(self):
        """ Renvoie l'état de l'IA """

        return self.Status

    def	select_commandes(self,indice):
        """ selectionne par indice notre commande """

    	if indice < 0 or indice > len(self.IA_commande):
    		return
    	return self.IA_commande[indice]


class Avancer:

    def __init__(self,vitesse,distance,robot):
        """ constructeur de notre classe Avancer
        initialisation de la vitesse de nos roues 
        initialisation de la distance à parcourir
        initialisation de notre robot pour lequel on applique la comande"""

        self.robot = robot
        self.vitesse = vitesse*3800
        self.distance = distance
        self.distance_parcouru = 0
        self.Status = True

    def update(self,dt) :
        """ Fais la mise à jour de notre déplacement en ligne droite """

        if self.distance_parcouru < self.distance:
            self.robot.set_motor_dps(self.vitesse,self.vitesse)
            position_move = self.distance_parcouru + math.sqrt(((self.robot.getmovex(dt)- self.robot.x)**2)+((self.robot.getmovey(dt)- self.robot.y)**2))*0.026
            if position_move > self.distance:
                self.robot.set_motor_dps(self.vitesse/10,self.vitesse/10)
            self.distance_parcouru += math.sqrt(((self.robot.getmovex(dt)- self.robot.x)**2)+((self.robot.getmovey(dt)- self.robot.y)**2))*0.026
            print("j'ai fini de parcourir "+str(self.distance_parcouru)+" cm")
        else:
            self.distance_parcouru = 0
            self.stop()

    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.Status

    def start(self):
        """ Lance la commande """

        self.Status = True

    def stop(self):
        """ Arret de la commande en cours"""

        self.Status = False
			
class Reculer:

    def __init__(self,vitesse,distance,robot):
        """ constructeur de notre classe Reculer
        initialisation de la vitesse de nos roues 
        initialisation de la distance à parcourir
        initialisation de notre robot pour lequel on applique la comande"""

        self.robot = robot
        self.vitesse = -vitesse*3800
        self.distance = distance
        self.distance_parcouru = 0
        self.Status = True

    def update(self,dt) :
        """ Fais la mise à jour de notre déplacement en ligne droite """

        if self.distance_parcouru < self.distance:
            self.robot.set_motor_dps(self.vitesse,self.vitesse)
            self.distance_parcouru += abs((self.robot.getmovex(dt)+self.robot.getmovey(dt)) - (self.robot.x + self.robot.y))
            print("j'ai fini de parcourir "+str(self.distance_parcouru)+" cm")
        else:
            self.distance_parcouru = 0
            self.stop()
    
    def getStatus(self):
        """ Renvoie l'état de notre commande """

        return self.Status

    def start(self):
        """ Lance notre commande """

        self.Status = True

    def stop(self):
        """ Arrête la commande en cours """

        self.Status = False

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
        self.Status = True

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
                self.robot.servo_rotate(angle)
                print("j'ai fini de parcourir "+str(self.angle_parcouru)+" degré")
        else:
            self.angle_parcouru = 0
            self.stop()

    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.Status

    def start(self):
        """ Lance la commande """

        self.Status = True

    def stop(self):
        """ Arrête la commande en cours """

        self.Status = False
        



class Square:

    def __init__(self,Robot):
        """ Constructeur de la classe Square, commande pour faire un carrée 
        initialisation du robot pour lequel on applique la commande
        initialisation de l'état de la commande 
        initialisation de la capacité d'aller tout droit 
        initilisation de la capcité de tourner à gauche
         """

        self.robot = Robot
        self.ToutDroit = Avancer(0.03,6,self.robot)
        self.TournerGauche = Tourner(0,90,30,self.robot)
        self.count = 0
        self.Status = True
			 
    def stop(self):
        """ Arrête la commande en cours """

        self.Status = False

    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.Status

    def start(self):
        """ Lance la commande """

        self.Status = True
        
    def update(self,dt):
        """ Fais la mise à jour de notre commande """

        if self.count == 8 or self.Status == False:
            self.stop()
        else:
            if self.ToutDroit.getStatus() == True:
                self.ToutDroit.update(dt)
            else:
                if self.TournerGauche.getStatus() == True:
                    self.TournerGauche.update(dt)
                else:
                    self.count += 2
                    self.ToutDroit.start()
                    self.TournerGauche.start()            


class Triangle:

    def	__init__(self,robot):
        """ Constructeur de notre classe Triangle, pour tracer un Trinagle
        initilisation du robot pour lequel on applique la commande
        initialisation de l'état de la commande 
        initialisation de la capacité d'aller tout droit 
        initilisation de la capcité de tourner à gauche
         """
         
        self.robot = robot
        self.TournerTriangle = Tourner(0,120,30,self.robot)
        self.ToutDroit = Avancer(0.03,8,self.robot)
        self.count = 0
        self.Status = True

    def start(self):
        """ Lance la commande """

        self.Status = True
				
    def stop(self):
        """ Arrête la commande en cours """

        self.Status = False

    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.Status
		
    def update(self,dt):
        """ Fais la mise à jour de la commande """
        
        if self.count == 6 or self.Status == False:
            self.stop()
        else:
            if self.ToutDroit.getStatus() == True:
                self.ToutDroit.update(dt)
            else:
                if self.TournerTriangle.getStatus() == True:
                    self.TournerTriangle.update(dt)
                else:
                    self.count += 2
                    self.ToutDroit.start()
                    self.TournerTriangle.start()
