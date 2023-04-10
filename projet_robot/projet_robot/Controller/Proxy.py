import time
import math

#partie simulation : 
largeur_robot = 60
diametre_roue = 7
portee_senseur = 30
circonference_robot = math.pi * diametre_roue
#parti réelle : 
WHEEL_BASE_WIDTH         = 117/10  # distance (mm) de la roue gauche a la roue droite.
WHEEL_DIAMETER           = 66.5/10 #  diametre de la roue (mm)
WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)
    

class   Proxy_simulation:

    def __init__(self,robot,vitesse,angle,simul):
        self.robot = robot
        self.angle = angle
        self.simul = simul
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
        if self.simul.detection_collision() or self.simul.detection_collision_bord_map_robot():
            self.simul.stop()

    
    def get_distance_parcourue(self):
        return self.distance_parcourue
    
    def reinitialiser_angle_parcouru(self):
        self.angle_parcouru = 0
    
    def update_angle_parcouru(self,dt):
        if self.simul.detection_collision() or self.simul.detection_collision_bord_map_robot():
            self.simul.stop()

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
        distance_roue_gauche = (new_pos_motor[0]*math.pi*WHEEL_DIAMETER*dt)/360
        distance_roue_droite = (new_pos_motor[1]*math.pi*WHEEL_DIAMETER*dt)/360
        self.distance_parcourue += (distance_roue_gauche+distance_roue_droite)/2
        

    def update_angle_parcouru(self,dt):
        previous_pos = (0,0)
        curr_pos = self.robot.get_motor_position()
        diff_pos = [curr_pos[i]-previous_pos[i] for i in range(2)]
        angle_rotated = [WHEEL_CIRCUMFERENCE*dt*(diff_pos[i]/360) for i in range(2)]
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

    def reset(self):
        self.robot.offset_motor_encoder(0+1,0)

    def tourner(self):
  
        if self.angle >= 0:
            self.robot.set_motor_dps(self.vitesse,-self.vitesse)
        else:
            self.robot.set_motor_dps(-self.vitesse,self.vitesse)    

    def avancer(self):
        self.robot.set_motor_dps(self.vitesse,self.vitesse)