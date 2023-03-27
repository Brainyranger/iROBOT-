import math
from projet_robot.Controller.Proxy_IA import largeur_robot,diametre_roue


class Robot:
    
  

    def __init__(self,x,y,angle) -> None: 
        """ Initialise le robot en une position (x,y) ,un angle ,et une vitesse (roue gauche et droite) """
        self.x  = x
        self.y  = y
        self.angle  = angle*math.pi/180 #conversion degré par seconde en radian par seconde
        self.motor_left  = 0 
        self.motor_right = 0 
        self.LED_LEFT_EYE = (255,0,0)
        self.LED_RIGHT_EYE = (0,0,255)
        

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
            
    def set_led(self):
        """ alterner les deux leds """
        tmp = self.LED_LEFT_EYE 
        self.LED_LEFT_EYE = self.LED_RIGHT_EYE
        self.LED_RIGHT_EYE = tmp 

    def move_angle(self, angle,direction):
        """ Tourne le robot a l'angle en parametre """
        pass

    def getAngleEnDegre(self):
        """ Renvoie l'angle dur robot en degré"""
        pass

    def getmovex(self,dt):
        """ Simule le déplacement du robot en x selon un temps dt """
        pass
    def getmovey(self,dt):
        """ Simule le déplacement du robot en y selon un temps dt """
        pass

    def set_led_left(self,colour):
        """change la couleur led gauche"""
        pass
        
    def set_led_right(self,colour):
        """change la couleur led droite"""
        pass
        
    def move(self,dt):
        """ Deplace le robot selon x et y et modifie son angle """
        pass
