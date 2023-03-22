from projet_robot.Simulation.Robot import Robot

class Decorateur_robot_reel(Robot)

    def __init__(self,robot)->None:
    	self.robot = robot
	self.x = 50
	self.y = 300
	self.angle  = 0 #conversion degré par seconde en radian par seconde

    def move(self,dt):
        """ Deplace le robot selon x et y et modifie son angle """
        self.x += ((self.robot.motor_left+self.robot.motor_right)/2)*math.cos(self.angle)*dt
        self.y -= ((self.robot.motor_left+self.robot.motor_right)/2)* math.sin(self.angle)*dt
        self.angle += (self.robot.motor_left - self.robot.motor_right) / (largeur_robot + 2*diametre_roue)*dt
   
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

