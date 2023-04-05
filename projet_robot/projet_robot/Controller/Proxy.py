import time
import math

#partie simulation : 
largeur_robot = 60
diametre_roue = 7
portee_senseur = 30
circonference_robot = math.pi * diametre_roue
#parti réelle : 
WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)
    

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

    def set_led_left(self,colour):
        """change la couleur led gauche"""
        
        self.LED_LEFT_EYE = colour
        
    def set_led_right(self,colour):
        """change la couleur led droite"""
        
        self.LED_RIGHT_EYE = colour
           
    def reset(self):
        self.robot.offset_motor_encode("self.motor_left+self.motor_right",0)

    
    def tourner(self,vitesse):
  
        if self.angle >= 0:
            self.robot.set_motor_dps(vitesse,-vitesse)
        else:
            self.robot.set_motor_dps(-vitesse,vitesse)    

    def avancer(self,vitesse,dt):
        self.robot.set_motor_dps(vitesse,vitesse)

 
class   Proxy_reel:

    def __init__(self,robot):
        self.robot = robot

    def	__getattr__(self,attr):
    	return  getattr(self.robot,attr)

    def update_distance_parcourue(self):
        posl = 0
        posr = 0
        new_pos_motor = self.robot.get_motor_position()
        distance_roue_gauche = (new_pos_motor[0]-posl)*math.pi*diametre_roue
        distance_roue_droite = (new_pos_motor[1]-posr)*math.pi*diametre_roue
        posl = new_pos_motor[0]
        posr = new_pos_motor[1]
        distance_parcouru = (distance_roue_gauche+distance_roue_droite)/2
        return distance_parcouru

    def update_angle_parcouru(self):
        previous_pos = (0,0)
        curr_pos = self.robot.get_motor_position()
        diff_pos = [curr_pos[i]-previous_pos[i] for i in range(2)]
        angle_rotated = [WHEEL_CIRCUMFERENCE*(diff_pos[i]/360) for i in range(2)]
        angle_parcouru = (angle_rotated[0]+angle_rotated[1])/2
        return angle_parcouru

    def reset(self):
        self.robot.offset_motor_encode(self.MOTOR_LEFT,self.read_encoders()[0])
        self.robot.offset_motor_encode(self.MOTOR_RIGHT,self.read_encoders()[1])

    def tourner(self,vitesse):
        if self.angle >= 0:
            self.robot.set_motor_dps(0,vitesse)
            self.robot.set_motor_dps(1,-vitesse)
        else:
            self.robot.set_motor_dps(0,-vitesse)
            self.robot.set_motor_dps(1,vitesse)    

    def avancer(self,vitesse,dt):
        self.robot.set_motor_dps(0+1,vitesse)

