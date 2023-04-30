import math
from projet_robot.Controller.Constante import WHEEL_BASE_CIRCUMFERENCE,WHEEL_DIAMETER,diametre_roue,largeur_robot   
from projet_robot.Simulation.Environnement import Environnement as Simul

class Proxy:
    """initialisation de notre Proxy pour un robot"""
    def __init__(self,robot):
        self.robot = robot
    
    def	__getattr__(self,attr):
    	return  getattr(self.robot,attr)
    

class   Proxy_simulation(Proxy):

    def __init__(self,robot,vitesse,angle):
        """initialisation du proxy du robot virtuel
        initialisation de son orientation 
        initilisation de sa vitesse """
        Proxy.__init__(self,robot)
        self.angle = angle
        self.robot.get_distance = Simul.detection_obstacle()
        self.vitesse = vitesse*3800
        self.acc_left = 0
        self.acc_right = 0
        self.distance_parcourue = 0
        self.angle_parcouru = 0
        
    
    def reinitialiser_distance_parcourue(self):
        """Réinitialise la distance parcourue par le robot"""
        self.distance_parcourue = 0
    
    def update_distance_parcourue(self,dt):
        """Fais la mise à jour de la distance parcourue"""
        distance_roue_gauche = (self.vitesse*dt*2*math.pi*diametre_roue/2)/360
        distance_roue_droite = (self.vitesse*dt*2*math.pi*diametre_roue/2)/360
        self.distance_parcourue += (distance_roue_gauche+distance_roue_droite)/2

    def get_distance_parcourue(self):
        """ Renvoie la distance parcourue"""
        return self.distance_parcourue
    
    def reinitialiser_angle_parcouru(self):
        """Réinitialise l'angle parcourue"""
        self.angle_parcouru = 0
    
    def update_angle_parcouru(self,dt):
        """Fais la mise à jour de l'angle parcouru"""
        self.angle_parcouru += self.vitesse*dt/2*math.pi
        
    def get_angle_parcouru(self):
        """Renvoie l'angle parcourue"""
        return self.angle_parcouru

    def set_led_left(self,colour):
        """change la couleur led gauche par une couleur passée en paramètre"""
        self.LED_LEFT_EYE = colour
        
    def set_led_right(self,colour):
        """change la couleur led droite par une couleur passée en paramètre"""
        self.LED_RIGHT_EYE = colour
           
    def reset(self):
        """Réinitialise la position des roues"""
        self.robot.offset_motor_encoder("self.motor_left+self.motor_right",0)

    
    def tourner(self):
        """Fais tourner le robot"""
        if self.angle >= 0:
            self.robot.set_motor_dps(self.vitesse,-self.vitesse)
        else:
            self.robot.set_motor_dps(-self.vitesse,self.vitesse)    

    def avancer(self):
        """Fais avancer le robot"""
        self.robot.set_motor_dps(self.vitesse,self.vitesse)

    def stop(self):
        """ Arrête le robot"""
        self.robot.set_motor_dps(0,0)
    
    def get_distance(self):
        """Renvoie la distance entre le robot et l'obstacle"""
        return self.robot.get_distance()
    
    def update_acceleration(self,dt):
        """ Fais la mise à jour de l'accélaration du robot"""
        new_pos = self.robot.get_motor_position()
        self.acc_left += (new_pos[0]*dt)*9.81
        self.acc_right += (new_pos[1]*dt)*9.81
        self.distance_parcourue = self.acc_left

    def avancer_accelerator(self):
        """Accélère notre robot"""
        self.robot.set_motor_dps(self.acc_left,self.acc_right)

class   Proxy_reel(Proxy):

    def __init__(self,robot,vitesse,angle):
        """initialisation du proxy du robot réel
        initialisation de son orientation 
        initilisation de sa vitesse """
        Proxy.__init__(self,robot)
        self.vitesse = vitesse*100
        self.angle = angle
        self.distance_parcourue = 0
        self.angle_parcouru = 0
        self.acc_left = 0
        self.acc_right = 0
    

    def update_distance_parcourue(self,dt):
        """Fais la mise à jour de la distance parcourue"""
        new_pos_motor = self.robot.get_motor_position()
        distance_roue_gauche = abs(new_pos_motor[0]*math.pi*(WHEEL_DIAMETER/10)*dt)/360
        distance_roue_droite = abs(new_pos_motor[1]*math.pi*(WHEEL_DIAMETER/10)*dt)/360
        self.distance_parcourue += (distance_roue_gauche+distance_roue_droite)/2

    def update_angle_parcouru(self,dt):
        """Fais la mise à jour de l'angle parcouru"""
        new_pos_motor = self.robot.get_motor_position()
        distance_roue_gauche = abs(new_pos_motor[0]*math.pi*(WHEEL_DIAMETER/10)*dt)/360
        distance_roue_droite = abs(new_pos_motor[1]*math.pi*(WHEEL_DIAMETER/10)*dt)/360
        self.distance_parcourue += (distance_roue_gauche+distance_roue_droite)/2

    def reset(self):
        """Réinitialise la position des roues"""
        self.robot.offset_motor_encoder(1,self.robot.read_encoders()[0])
        self.robot.offset_motor_encoder(2,self.robot.read_encoders()[1])
    
    def reinitialiser_distance_parcourue(self):
        """Réinitialise la distance parcourue par le robot"""
        self.distance_parcourue = 0
    
    def get_distance_parcourue(self):
        """ Renvoie la distance parcourue"""
        return self.distance_parcourue
    
    def reinitialiser_angle_parcouru(self):
        """Réinitialise l'angle parcourue"""
        self.angle_parcouru = 0

        
    def get_angle_parcouru(self):
        """Renvoie l'angle parcourue"""
        return self.angle_parcouru


    def tourner(self):
        """Fais tourner le robot"""
        if self.angle >= 0:
            self.robot.set_motor_dps(2,self.vitesse)
            self.robot.set_motor_dps(1,-self.vitesse)
        else:
            self.robot.set_motor_dps(2,-self.vitesse)
            self.robot.set_motor_dps(1,self.vitesse)
    def avancer(self):
        """Fais avancer le robot"""
        self.robot.set_motor_dps(1+2,self.vitesse)

    def stop(self):
        """Arrête le robot"""
        self.robot.set_motor_dps(1+2,0)
    
    def get_distance(self):
        return self.robot.get_distance()
    
    def update_acceleration(self,dt):
        """ Fais la mise à jour de l'accélaration du robot"""
        new_pos = self.robot.get_motor_position()
        self.acc_left += (new_pos[0]*dt)*9.81
        self.acc_right += (new_pos[1]*dt)*9.81
        self.distance_parcourue = self.acc_left

    def avancer_accelerator(self):
        """Accélère notre robot"""
        self.robot.set_motor_dps(1+2,self.acc_left)