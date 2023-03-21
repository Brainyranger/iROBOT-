
import math

class Constante:

largeur_robot = 60
diametre_roue = 7
portee_senseur = 30
circonference_robot = math.pi * diametre_roue

class   Decorator:

    def __init__(self,robot):
        """ classe Decorator qui ajoute des méthodes à appliquer sur l'API du robot 
             initialisation de notre robot"""

        self.robot = robot
        
    def	__getattr__(self,attr):
        """ renvoie les attributs du robot """

    	return  getattr(self.robot,attr)
	

class	Avancer_Decorator(Decorator):

    def __init__(self,robot):
        Decorator.__init__(self,robot)
   
    	
    def nb_tour(self,distance):
        return distance/circonference_robot
    
    def getdegre_rotation(self,distance):
        valeur = Avancer_Decorator.nb_tour(self,distance)*360
        return valeur
    	
class	Tourner_Decorator(Decorator):
    
    def __init__(self,robot):
        """ classe Tourner_Decorator qui hérite de Decorator
         initialise un robot et lui octroie de nouvelle méthodes pour la commande 
         Tourner """
        Decorator.__init__(self,robot) 
               
    def tourner(self,speed,dps,dt):
        """ fais tourner les roues du robot sans vitesse """

        self.robot.move_angle(self.dps*dt)
        self.robot.set_motor_dps(0,0)
	    
    def tourner2(self,speed,angle,dps,dt):
        """ fais tourner le robot selon les vitesses de rotation des roues """

        self.robot.set_motor_dps(speed*(1+(angle/90)),speed*(1-(angle/90)))
        self.robot.move_angle(dps*dt)
        
    def dist_turn(self,vitesse,angle,dt):
        """ renvoie la distance parcourue en cm à chaque instant dt en fonction d'un angle de rotation """
         
        return ((vitesse*(1-(angle/90))+vitesse*(1+(angle/90)))/2)*dt*(angle/360)
       
	
  
