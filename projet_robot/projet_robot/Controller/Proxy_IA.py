import math

largeur_robot = 60
diametre_roue = 7
portee_senseur = 30
circonference_robot = math.pi * diametre_roue

class   Proxy_simulation:

    def __init__(self,robot):
        self.robot = robot
        
    def	__getattr__(self,attr):
    	return  getattr(self.robot,attr)
        
    def get_distance_parcourue(self,dt):
        posx1 = self.robot.x
        posy1 = self.robot.y
        posx2 = self.robot.getmovex(dt)
        posy2 = self.robot.getmovey(dt)
        return math.sqrt((posx2-posx1)**2+(posy2-posy1)**2)*0.026
   
    def move(self,dt):
        """ Deplace le robot selon x et y et modifie son angle """
        self.x += ((self.motor_left + self.motor_right)/2) * math.cos(self.angle)*dt
        self.y -= ((self.motor_left + self.motor_right)/2) * math.sin(self.angle)*dt
        self.angle += ((self.motor_left - self.motor_right) / (largeur_robot + 2*diametre_roue))*dt

    
    def move_angle(self, angle,direction):
        """ Tourne le robot a l'angle en parametre """
        if direction == "gauche":
            self.angle += angle*math.pi/180
            if self.angle > 2*math.pi:
                self.angle -= 2*math.pi
        else:
            self.angle -= angle*math.pi/180
            self.angle += 2*math.pi
          

    def getAngleEnDegre(self):
        """ Renvoie l'angle dur robot en degré"""
        return self.angle*180/math.pi

    def getmovex(self,dt):
        """ Simule le déplacement du robot en x selon un temps dt """
        return (self.x+((self.motor_left+self.motor_right)/2)*math.cos(self.angle)*dt) 

    def getmovey(self,dt):
        """ Simule le déplacement du robot en y selon un temps dt """
        return (self.y-((self.motor_left+self.motor_right)/2)*math.sin(self.angle)*dt)
    
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
