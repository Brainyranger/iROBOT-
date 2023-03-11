

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

    def getAngleEnDegre(self):
        """ Renvoie l'angle dur robot en degré"""
        return self.angle*180/math.pi

    def getmovex(self,dt):
        """ Simule le déplacement du robot en x selon un temps dt """
        return (self.x+((self.motor_left+self.motor_right)/2)*math.cos(self.angle)*dt) 

    def getmovey(self,dt):
        """ Simule le déplacement du robot en y selon un temps dt """
        return (self.y-((self.motor_left+self.motor_right)/2)*math.sin(self.angle)*dt)

    def get_distance_parcourue(self,posx1,posy1,posx2,posy2):
        return math.sqrt((posx2-posx1)**2+(posy2-posy1)**2)*0.026
        