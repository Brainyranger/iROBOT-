import math,time
from projet_robot.Simulation.Robot import Robot


largeur_robot = 60
diametre_roue = 7
portee_senseur = 30
circonference_robot = math.pi * diametre_roue

class Proxy:

    def __init__(self,robot)->None:
        self.robot = robot
        self.x = 50
        self.y = 300
        self.angle  = 0
        self.angle_parcouru = 0
        self.distance_parcourue = 0
        self.angle_parcouru = 0

    def reinitialiser_distance_parcourue(self):
        self.distance_parcourue = 0

    def reinitialiser_angle_parcouru(self):
        self.angle_parcouru = 0
    
    def move(self,dt):
        """ Deplace le robot selon x et y et modifie son angle """
        posx1 = self.x
        posy1 = self.y
        self.x += ((self.robot.motor_left+self.robot.motor_right)/2)*math.cos(self.angle)*dt
        self.y -= ((self.robot.motor_left+self.robot.motor_right)/2)* math.sin(self.angle)*dt
        self.angle += (self.robot.motor_left - self.robot.motor_right) / (largeur_robot + 2*diametre_roue)*dt
        posx2 = self.x
        posy2 = self.y
        self.distance_parcourue += math.sqrt((posx2-posx1)**2+(posy2-posy1)**2)*0.026
   
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
        return ((self.robot.motor_left+self.robot.motor_right)/2)*math.cos(self.angle)*dt

    def getmovey(self,dt):
        """ Simule le déplacement du robot en y selon un temps dt """
        return ((self.robot.motor_left+self.robot.motor_right)/2)*math.sin(self.angle)*dt

    def set_led_left(self,colour):
        """change la couleur led gauche"""
        
        self.LED_LEFT_EYE = colour
        
    def set_led_right(self,colour):
        """change la couleur led droite"""
        
        self.LED_RIGHT_EYE = colour
           
    def vitesse_rotation_gauche(self,vitesse,angle):
        return vitesse*(1-(angle)/90)

    def vitesse_rotation_droite(self,vitesse,angle):
        return vitesse*(1+(angle)/90)

    def get_distance_parcourue(self):
        posl = 0
        posr = 0
        new_pos_motor = self.robot.get_motor_position()
        distance_roue_gauche = (new_pos_motor[0]-posl)*math.pi*WHEEL_DIAMETER 
        distance_roue_droite = (new_pos_motor[1]-posr)*math.pi*WHEEL_DIAMETER 
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