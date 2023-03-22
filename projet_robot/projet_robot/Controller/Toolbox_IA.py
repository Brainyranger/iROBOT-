
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
        Decorator.__init__(self,robot)
        self.angle
        
    def get_distance_parcourue(self):
        rayon_braquage = abs(largeur_robot/math.tan(self.angle))
        arc_pisur2 = 0.25*2*math.pi
        dist_une_roue = (rayon_braquage*arc_pisur2)/2
        constante_de_correction = 4.5
        return dist_une_roue - constante_de_correction
               
        
    def nb_tour(self):
        return (Tourner_Decorator.get_distance_parcourue(self)/circonference_robot)
    
    def getdegre_rotation(self):
        return Tourner_Decorator.nb_tour(self)*360
       
	
  
