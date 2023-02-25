import math

global WHEEL_DIAMETER 
global WHEEL_BASE_WIDTH   
WHEEL_DIAMETER = 5
WHEEL_BASE_WIDTH= 40

class Robot:
    
  

    def __init__(self,x,y,angle) -> None: 
        """ Initialise le robot avec une position en x et en y, une orientation et une vitesse pour la roue gauche et droite"""
        self.x  = x
        self.y  = y
        self.angle  = angle
        self.motor_left  = 0 
        self.motor_right = 0 
        
    def move(self,dt):
        """ Déplace le robot en fonction d'un temps donné """
        self.x += ((self.motor_left + self.motor_right)/2) * math.cos(self.angle)*dt
        self.y -= ((self.motor_left + self.motor_right)/2) * math.sin(self.angle)*dt
        self.angle += (self.motor_left - self.motor_right) / (WHEEL_BASE_WIDTH + 2*WHEEL_DIAMETER)*dt


    def set_motor_dps(self, motor_left, motor_right):
        """ Fixe la vitesse d'un moteur """
        self.motor_left = motor_left
        self.motor_right = motor_right

    
    def servo_rotate(self, angle):
        """ Tourne le robot a l'angle en parametre """
        self.angle += angle

    def getmovex(self,dt):
        """ Renvoie la position en x du robot au prochain déplacement """
        return (self.x+((self.motor_left+self.motor_right)/2)*math.cos(self.angle)*dt) 

    def getmovey(self,dt):
        """ Renvoie la position en y du robot au prochain déplacement """
        return (self.y-((self.motor_left+self.motor_right)/2)*math.sin(self.angle)*dt)