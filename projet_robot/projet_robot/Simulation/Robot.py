import math
from projet_robot.Controller.Constante import largeur_robot,diametre_roue
class Robot:
    
  

    def __init__(self,x,y,angle,fps,nb_im,resolution) -> None: 
        """ Initialise le robot en une position (x,y) ,un angle ,et une vitesse (roue gauche et droite) """
        self.x  = x
        self.y  = y
        self.fps = fps
        self.nb_im = nb_im
        self.size_im = resolution
        self.angle  = math.radians(angle) #conversion degré par seconde en radian par seconde
        self.motor_left  = 0 
        self.motor_right = 0 
        self.LED_LEFT_EYE = (255,0,0)
        self.LED_RIGHT_EYE = (0,0,255)
        

    def set_motor_dps(self, motor_left, motor_right):
        """ Fixe la vitesse d'un moteur """
        self.motor_left = motor_left
        self.motor_right = motor_right
        
    def offset_motor_encoder(self, port, offset):
        """
        Fixe l'offset des moteurs (en degres) (permet par exemple de reinitialiser a 0 l'etat 
        """
        if port == "self.motor_left":
            self.motor_left = offset
        elif port == "self.motor_right":
            self.motor_right = offset
        elif port == "self.motor_right+self.motor_left":
            self.motor_left = offset
            self.motor_right = offset
        else:
            return 
            
    def set_led(self):
        """ Alterne les deux leds du robot """
        tmp = self.LED_LEFT_EYE 
        self.LED_LEFT_EYE = self.LED_RIGHT_EYE
        self.LED_RIGHT_EYE = tmp 

    def move(self,dt):
        """ Fais la mise à jour du déplacement du robot dans la simulaton"""
        self.x += ((self.motor_left + self.motor_right)/2) * math.cos(self.angle)*dt
        self.y -= ((self.motor_left + self.motor_right)/2) * math.sin(self.angle)*dt
        self.angle += ((self.motor_left - self.motor_right) / (largeur_robot + 2*diametre_roue))*dt

    def move_angle(self,angle):
        """ Tourne le robot en fonction de l'angle passé en parametre """
        self.angle += angle*math.pi/180
        if self.angle > 2*math.pi:
            self.angle -= 2*math.pi
    
    def set_led_left(self,color):
        """change la couleur led gauche"""
        pass
        
    def set_led_right(self,color):
        """change la couleur led droite"""
        pass
        
    def get_distance_parcourue(self):
        pass
    
    def get_angle_parcouru(self):
        pass

    def get_distance(self):
        pass

    def get_image(self,cpt):
        pass

    def start_recording(self):
        pass

    def stop_recording(self):
        pass

    def update_recording(self,dt):
        pass