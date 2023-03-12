

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
	
class	Avancer_decorator(Decorator):

    def	__init__(self):
	    self.angle = 0
	    self.distance_parcouru = 0
	    self.position_move = 0

        def get_distance_parcourue(self,posx1,posy1,posx2,posy2):
        return math.sqrt((posx2-posx1)**2+(posy2-posy1)**2)*0.026
     
     
    def aupas(self,dt):
        self.robot.set_motor_dps(self.vitesse/10,self.vitesse/10)
        self.distance_parcouru += math.sqrt(((self.robot.getmovex(dt)- self.robot.x)**2)+((self.robot.getmovey(dt)- self.robot.y)**2))*0.026

    def	avancer(self,dt):
        if self.position_move > self.distance:
        	return self.aupas(dt)