import math
from projet_robot.Controller.Toolbox_IA import largeur_robot,diametre_roue


class Robot:
    
  

    def __init__(self,x,y,angle) -> None: 
        """ Initialise le robot en une position (x,y) ,un angle ,et une vitesse (roue gauche et droite) """
        self.motor_left  = 0 
        self.motor_right = 0 


    def set_motor_dps(self, motor_left, motor_right):
        """ Fixe la vitesse d'un moteur """
        self.motor_left = motor_left
        self.motor_right = motor_right


    def get_motor_position(self):
        """
        Lit les etats des moteurs en degre.
        :return: couple du  degre de rotation des moteurs
        """
        
      
        return (self.motor_left, self.motor_right)
        
        
    def offset_motor_encoder(self, port, offset):
        """
        Fixe l'offset des moteurs (en degres) (permet par exemple de reinitialiser a 0 l'etat 
        """
        port = offset
            
