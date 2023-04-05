import math
from projet_robot.Controller.Proxy import largeur_robot,diametre_roue
class Robot:
    
  

    def __init__(self,x,y,angle) -> None: 
        """ Initialise le robot en une position (x,y) ,un angle ,et une vitesse (roue gauche et droite) """
        self.x  = x
        self.y  = y
        self.angle  = math.radians(angle) #conversion degré par seconde en radian par seconde
        self.motor_left  = 0 
        self.motor_right = 0 
        self.distance_parcourue = 0
        self.angle_parcouru = 0
        self.LED_LEFT_EYE = (255,0,0)
        self.LED_RIGHT_EYE = (0,0,255)
        

    def set_motor_dps(self, motor_left, motor_right):
        """ Fixe la vitesse d'un moteur """
        self.motor_left = motor_left
        self.motor_right = motor_right



        
    def offset_motor_encoder(self, port, offset):
        """
        Fixe l'offset des moteurs (en degres) (permet par exemple de reinitialiser a 0 l'etat 
        """
        if port == "self.motor_left":
            self.robot.motor_left = offset
        elif port == "self.motor_right":
            self.robot.motor_right = offset
        elif port == "self.motor_right+self.motor_left":
            self.robot.motor_left = offset
            self.robot.motor_right = offset
        else:
            return 


            
    def set_led(self):
        """ alterner les deux leds """
        tmp = self.LED_LEFT_EYE 
        self.LED_LEFT_EYE = self.LED_RIGHT_EYE
        self.LED_RIGHT_EYE = tmp 



    def getmovex(self,dt):
        """ Simule le déplacement du robot en x selon un temps dt """
        return (self.x+((self.motor_left+self.motor_right)/2)*math.cos(self.angle)*dt) 

    def getmovey(self,dt):
        """ Simule le déplacement du robot en y selon un temps dt """
        return (self.y-((self.motor_left+self.motor_right)/2)*math.sin(self.angle)*dt)
    

    def set_led_left(self,colour):
        """change la couleur led gauche"""
        pass
        
    def set_led_right(self,colour):
        """change la couleur led droite"""
        pass
        
    def move(self,dt):
        """ Deplace le robot selon x et y et modifie son angle """
        self.x += ((self.motor_left + self.motor_right)/2) * math.cos(self.angle)*dt
        self.y -= ((self.motor_left + self.motor_right)/2) * math.sin(self.angle)*dt
        self.angle += ((self.motor_left - self.motor_right) / (largeur_robot + 2*diametre_roue))*dt

    def get_distance_parcourue(self):
        pass
    
    def get_angle_parcouru(self):
        pass

    def move_angle(self,angle):
        """ Tourne le robot a l'angle en parametre """
        self.angle += angle*math.pi/180
        if self.angle > 2*math.pi:
            self.angle -= 2*math.pi



class   Vision:

    def __init(self,robot,nb_img,resolution,fps):
        self.robot = robot
        self.nb_img = nb_img
        self.img_queue = None
        self.resolution = resolution
        self.fps = fps


    def start_recording(self):
        cv2.VideoCapture(0)

    def stop_recording(self):
        cv2.VideoCapture(0).realease()
        cv2.destroyAllwindows()
        
    def get_image(self,img,indice):
        cv2.imshow('image'+str(indice),img)

    def get_images(self,imgs):
        for i in range(0,len(imgs)):
            self.get_image(imgs[i],i)

    def read_image(self,img):
        pass

    def gray_image(self,img):
        pass

    def get_mask_image(self,img,mask):
        pass
    
    def detection_contour(self,largeur,hauteur):
        pass

    def find_contour(self,contour):
        pass

