import time
import math
from projet_robot.Controller.Robot_Mockup import WHEEL_BASE_CIRCUMFERENCE,WHEEL_BASE_WIDTH,WHEEL_DIAMETER

#partie simulation : 
largeur_robot = 60
diametre_roue = 7
portee_senseur = 30
circonference_robot = math.pi * diametre_roue


    

class   Proxy_simulation:

    def __init__(self,robot,vitesse,angle):
        self.robot = robot
        self.angle = angle
        self.vitesse = vitesse*3800
        self.distance_parcourue = 0
        self.angle_parcouru = 0
        

    def	__getattr__(self,attr):
    	return  getattr(self.robot,attr)
    
    def reinitialiser_distance_parcourue(self):
        self.distance_parcourue = 0
    
    def update_distance_parcourue(self,dt):
        distance_roue_gauche = (self.vitesse*dt*2*math.pi*diametre_roue/2)/360
        distance_roue_droite = (self.vitesse*dt*2*math.pi*diametre_roue/2)/360
        self.distance_parcourue += (distance_roue_gauche+distance_roue_droite)/2

    
    def get_distance_parcourue(self):
        return self.distance_parcourue
    
    def reinitialiser_angle_parcouru(self):
        self.angle_parcouru = 0
    
    def update_angle_parcouru(self,dt):

        self.angle_parcouru += self.vitesse*dt/2*math.pi
        
    def get_angle_parcouru(self):
        return self.angle_parcouru

    def set_led_left(self,colour):
        """change la couleur led gauche"""
        
        self.LED_LEFT_EYE = colour
        
    def set_led_right(self,colour):
        """change la couleur led droite"""
        
        self.LED_RIGHT_EYE = colour
           
    def reset(self):
        self.robot.offset_motor_encoder("self.motor_left+self.motor_right",0)

    
    def tourner(self):
  
        if self.angle >= 0:
            self.robot.set_motor_dps(self.vitesse,-self.vitesse)
        else:
            self.robot.set_motor_dps(-self.vitesse,self.vitesse)    

    def avancer(self):
        self.robot.set_motor_dps(self.vitesse,self.vitesse)

    

class   Proxy_reel:

    def __init__(self,robot,vitesse,angle):
        self.robot = robot
        self.vitesse = vitesse*100
        self.angle = angle
        self.distance_parcourue = 0
        self.angle_parcouru = 0
    

    def	__getattr__(self,attr):
    	return  getattr(self.robot,attr)

    def update_distance_parcourue(self,dt):
        new_pos_motor = self.robot.get_motor_position()
        distance_roue_gauche = (new_pos_motor[0]*math.pi*(WHEEL_DIAMETER/10)*dt)/360
        distance_roue_droite = (new_pos_motor[1]*math.pi*(WHEEL_DIAMETER/10)*dt)/360
        self.distance_parcourue += (distance_roue_gauche+distance_roue_droite)/2
        

    def update_angle_parcouru(self,dt):
        previous_pos = (0,0)
        curr_pos = self.robot.get_motor_position()
        diff_pos = [curr_pos[i]-previous_pos[i] for i in range(2)]
        angle_rotated = [(WHEEL_BASE_CIRCUMFERENCE/10)*dt*(diff_pos[i]/360) for i in range(2)]
        self.angle_parcouru += (angle_rotated[0]+angle_rotated[1])/2


    def reset(self):
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT,self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT,self.robot.get_motor_position()[1])
    
    def reinitialiser_distance_parcourue(self):
        self.distance_parcourue = 0
    
    def get_distance_parcourue(self):
        return self.distance_parcourue
    
    def reinitialiser_angle_parcouru(self):
        self.angle_parcouru = 0

        
    def get_angle_parcouru(self):
        return self.angle_parcouru


    def tourner(self):
  
        if self.angle >= 0:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,self.vitesse)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,-self.vitesse)
        else:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,-self.vitesse)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,self.vitesse)

    def avancer(self):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,self.vitesse)

    def stop(self):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)