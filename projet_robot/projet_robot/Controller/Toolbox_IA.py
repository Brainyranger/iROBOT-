
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
        self.rayon_courbure = 60
        
    def get_distance_parcourue(self):
        return math.pi*2*self.rayon_courbure*0.25 
               
        
    def nb_tour(self):
        circonf = math.pi*7
        return (2*Tourner_Decorator.get_distance_parcourue(self)/circonf)
    
    def getdegre_rotation(self):
        #valeur = Tourner_Decorator.nb_tour(self)*360
        #pour tourner à gauche et droite = 320
        return 320
       
	
  
