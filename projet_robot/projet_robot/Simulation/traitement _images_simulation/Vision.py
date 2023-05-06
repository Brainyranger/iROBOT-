from PIL import ImageGrab
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


    def get_image(self):
        """ Renvoie une capture d'écran sous format JPEG """
        image = ImageGrab.grab() 
        image = image.resize(self.size)
        image.save(chemin_images_simulation+".jpeg","JPEG") 
    
    def update_recording(self):
        """ Fais un enregistrement d'images"""
        while(self.start_record):
            self.robot.get_image(chemin_images_simulation)
            time.sleep(self.dt)

    def stop_recording(self):
        """Arrête l'enregistrement d'images"""
        self.start_record = False
        self._thread_image.stop()

    def start_recording(self):
        """ lance l'enregistrement d'images"""
        self._thread_image = threading.Thread(target=self._start_record)
        self._thread_image.start()    
        
