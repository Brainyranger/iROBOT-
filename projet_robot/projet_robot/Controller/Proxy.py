import math,time
from projet_robot.Simulation.Robot import Robot

import math

largeur_robot = 60
diametre_roue = 7
portee_senseur = 30
circonference_robot = math.pi * diametre_roue
distance_parcourue = 0
angle_parcouru = 0

class   Proxy_simulation:

    def __init__(self,robot):
        self.robot = robot
        
    def	__getattr__(self,attr):
    	return  getattr(self.robot,attr)
    
    def reinitialiser_distance_parcourue(self):
        self.distance_parcourue = 0
    
    def update_distance_parcourue(self,dt):
        posx1 = self.robot.x
        posy1 = self.robot.y
        posx2 = self.robot.getmovex(dt)
        posy2 = self.robot.getmovey(dt)
        self.distance_parcourue += math.sqrt((posx2-posx1)**2+(posy2-posy1)**2)*0.026
        
    def get_distance_parcourue(self):
        return self.distance_parcourue
    
    def reinitialiser_angle_parcouru(self):
        self.angle_parcouru = 0
    
    def update_angle_parcouru(self,vitesse,dt):
        self.angle_parcouru += vitesse*dt/2*math.pi
        
    def get_angle_parcouru(self):
        return self.angle_parcouru
   
    def move(self,dt):
        """ Deplace le robot selon x et y et modifie son angle """
        self.x += ((self.motor_left + self.motor_right)/2) * math.cos(self.angle)*dt
        self.y -= ((self.motor_left + self.motor_right)/2) * math.sin(self.angle)*dt
        self.angle += ((self.motor_left - self.motor_right) / (largeur_robot + 2*diametre_roue))*dt

    
    def move_angle(self, angle,direction):
        """ Tourne le robot a l'angle en parametre """
        if direction == "gauche":
            self.angle += angle*math.pi/180
            if self.angle > 2*math.pi:
                self.angle -= 2*math.pi
        else:
            self.angle -= angle*math.pi/180
            self.angle += 2*math.pi
          

    def getAngleEnDegre(self):
        """ Renvoie l'angle dur robot en degré"""
        return self.angle*180/math.pi

    def getmovex(self,dt):
        """ Simule le déplacement du robot en x selon un temps dt """
        return (self.x+((self.motor_left+self.motor_right)/2)*math.cos(self.angle)*dt) 

    def getmovey(self,dt):
        """ Simule le déplacement du robot en y selon un temps dt """
        return (self.y-((self.motor_left+self.motor_right)/2)*math.sin(self.angle)*dt)
    
    def set_led_left(self,colour):
        """change la couleur led gauche"""
        
        self.LED_LEFT_EYE = colour
        
    def set_led_right(self,colour):
        """change la couleur led droite"""
        
        self.LED_RIGHT_EYE = colour
           

    def reset(self):
        self.robot.offset_motor_encode("self.motor_left+self.motor_right",0)

class   Proxy_VraiRobot:

    def __init__(self,robot):
        self.robot = robot

    def get_distance_parcourue(self):
        posl = 0
        posr = 0
        new_pos_motor = self.robot.get_motor_position()
        distance_roue_gauche = (new_pos_motor[0]-posl)*math.pi*diametre_roue 
        distance_roue_droite = (new_pos_motor[1]-posr)*math.pi*diametre_roue
        posl = new_pos_motor[0]
        posr = new_pos_motor[1]
        distance_parcouru = (distance_roue_gauche+distance_roue_droite)/2
        return distance_parcouru

    def get_angle_parcouru(self):
        previous_pos = (0,0)
        curr_pos = self.robot.get_motor_position()
        diff_pos = [curr_pos[i]-previous_pos[i] for i in range(2)]
        angle_rotated = [WHEEL_CIRCUMFERENCE*(diff_pos[i]/360) for i in range(2)]
        angle_parcouru = (angle_rotated[0]+angle_rotated[1])/2
        return angle_parcouru

    def reset(self):
        self.robot.offset_motor_encode(self.MOTOR_LEFT,self.read_encoders()[0])
        self.robot.offset_motor_encode(self.MOTOR_RIGHT,self.read_encoders()[1])