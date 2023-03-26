import time
import math

largeur_robot = 60
diametre_roue = 7
portee_senseur = 30
circonference_robot = math.pi * diametre_roue

class   Decorator:

    def __init__(self,robot):
        self.robot = robot
        
    def	__getattr__(self,attr):
    	return  getattr(self.robot,attr)
	

class	Avancer_Decorator(Decorator):

    def __init__(self,robot):
        Decorator.__init__(self,robot)
        
    def get_distance_parcourue(self,dt):
        posx1 = self.robot.x
        posy1 = self.robot.y
        posx2 = self.robot.getmovex(dt)
        posy2 = self.robot.getmovey(dt)
        return math.sqrt((posx2-posx1)**2+(posy2-posy1)**2)*0.026
     
   
    def	avancer(self,vitesse,dt):
        self.robot.set_motor_dps(vitesse,vitesse)
        
    def set_led(self):
        tmp = self.robot.LED_LEFT_EYE 
        self.robot.set_led_left(self.robot.LED_RIGHT_EYE)
        self.robot.set_led_right(tmp)
        time.sleep(0.1)

class	Tourner_Decorator(Decorator):
    
    def __init__(self,robot):
        Decorator.__init__(self,robot) 
               
    def tourner(self,speed,dps,dt,str):
        self.robot.move_angle(self.dps*dt,str)
        self.robot.set_motor_dps(0,0)
	    
    
       
	
  