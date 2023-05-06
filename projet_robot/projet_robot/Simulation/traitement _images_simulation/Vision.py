from PIL import *
import cv2
from projet_robot.Controller.Constante import chemin_images_simulation
import threading
import time

class Vision:

    def __init__(self,nb,fps,resolution):
        """Constructeur pour la vision d'un robot
         nb : nb images
         fps: nb images par seconde
         resolution : resolution de la caméra"""
        self._thread_image = None
        self.size = resolution
        self.dt = (1/fps)
        self.nb_image = nb


def get_image():
    """ Renvoie une capture d'écran sous format JPEG """
    image = cv2.VideoCapture(0)
    #image = image.resize(self.robot.size_im)
    _,im_capture= image.read()
    #cv2.imshow("captture",im_capture)
    #im_capture.save(chemin_images_simulation,"JPEG") 
    cv2.imwrite(chemin_images_simulation,im_capture)

get_image()