import math
from projet_robot.Controller.Toolbox_IA import largeur_robot,diametre_roue


class Robot:
    
  

    def __init__(self,x,y,angle) -> None: 
        """ Initialise le robot en une position (x,y) ,un angle ,et une vitesse (roue gauche et droite) """
        self.x  = x
        self.y  = y
        self.angle  = angle*math.pi/180 #conversion degré par seconde en radian par seconde
        self.motor_left  = 0 
        self.motor_right = 0 
        
    def move(self,dt):
        """ Deplace le robot selon x et y et modifie son angle """
        self.x += ((self.motor_left + self.motor_right)/2) * math.cos(self.angle)*dt
        self.y -= ((self.motor_left + self.motor_right)/2) * math.sin(self.angle)*dt
        self.angle += (self.motor_left - self.motor_right) / (largeur_robot + 2*diametre_roue)*dt

    def set_motor_dps(self, motor_left, motor_right):
        """ Fixe la vitesse d'un moteur """
        self.motor_left = motor_left
        self.motor_right = motor_right

    
    def move_angle(self, angle):
        """ Tourne le robot a l'angle en parametre """
        self.angle += angle*math.pi/180
        if self.angle > 2*math.pi:
            self.angle -= 2*math.pi

    def getAngleEnDegre(self):
        """ Renvoie l'angle dur robot en degré"""
        return self.angle*180/math.pi

    def getmovex(self,dt):
        """ Simule le déplacement du robot en x selon un temps dt """
        return (self.x+((self.motor_left+self.motor_right)/2)*math.cos(self.angle)*dt) 

    def getmovey(self,dt):
        """ Simule le déplacement du robot en y selon un temps dt """
        return (self.y-((self.motor_left+self.motor_right)/2)*math.sin(self.angle)*dt)

    def get_motor_position(self,distance):
        """
        Lit les etats des moteurs en degre.
        :return: couple du  degre de rotation des moteurs
        """
        
        degres_rotation = (distance/circonference_robot)*360
        self.motor_left= degres_rotation
        self.motor_right = degres_rotation
        return (self.motor_left, self.motor_right)