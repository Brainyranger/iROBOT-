import math


class Robot:


    def __init__(self,x,y,angle) -> None: 
        """ Initialise le robot en une position (x,y) ,un angle ,et une vitesse (roue gauche et droite) """

        self.motor_left  = 0 
        self.motor_right = 0 
        self.LED_LEFT_EYE = (255,0,0)
        self.LED_RIGHT_EYE = (0,0,255)
        

    def set_motor_dps(self, motor_left, motor_right):
        """ Fixe la vitesse d'un moteur """
        self.motor_left = motor_left
        self.motor_right = motor_right


    def get_motor_position(self):
        """
        Lit les etats des moteurs en degre.
        :return: couple du  degre de rotation des moteurs
        """
        
      
        return (self.motor_left, self.motor_right)
        
        
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

    def set_led_left(self,colour):
        """change la couleur led gauche"""
        pass
        
    def set_led_right(self,colour):
        """change la couleur led droite"""
        pass



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

