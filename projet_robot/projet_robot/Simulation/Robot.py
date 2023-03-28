import math


class Robot:


    def __init__(self,x,y,angle) -> None: 
        """ Initialise le robot en une position (x,y) ,un angle ,et une vitesse (roue gauche et droite) """

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
        if port == "self.motor_left":
            self.robot.motor_left = offset
        elif port == "self.motor_right":
            self.robot.motor_right = offset
        elif port == "self.motor_right+self.motor_left":
            self.robot.motor_left = offset
            self.robot.motor_right = offset
        else:
            return 
            
    def set_led(self):
        """ alterner les deux leds """
        tmp = self.LED_LEFT_EYE 
        self.LED_LEFT_EYE = self.LED_RIGHT_EYE
        self.LED_RIGHT_EYE = tmp 

    def set_led_left(self,colour):
        """change la couleur led gauche"""
        pass
        
    def set_led_right(self,colour):
        """change la couleur led droite"""
        pass


