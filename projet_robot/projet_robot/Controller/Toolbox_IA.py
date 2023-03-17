
import math

class Constante:

    def __init__(self):

    def getLargeurRobot():
        return 60
    def getDiametreRoue():
        return 7

    def getPorteeSenseur():
        return 30
    
    def getSizeObs():
        return 20


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
     
   
    def	avancer(self,dt):
        self.robot.set_motor_dps(self.vitesse,self.vitesse)

class	Tourner_Decorator(Decorator):
    
    def __init__(self,robot):
        Decorator.__init__(self,robot) 
               
    def tourner(self,dps,dt):
        self.robot.servo_rotate(self.dps*dt)
        self.robot.set_motor_dps(0,0)
	    
	def tourner2(self,speed,angle,dps,dt):
        
        self.robot.set_motor_dps(speed*(1+(angle/90)),speed*(1-(angle/90)))
        self.robot.servo_rotate(dps*dt)
        
    def dist_turn(self,vitesse,angle,dt):
        return ((vitesse*(1-(angle/90))+vitesse*(1+(angle/90)))/2)*dt*(angle/360)
        
	
  
