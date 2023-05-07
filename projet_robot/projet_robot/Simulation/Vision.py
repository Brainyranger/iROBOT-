from PIL import Image
import os.path
from projet_robot.Controller.Constante import chemin_images_simulation,chemin_images_reel

class Vision:

    def __init__(self,nb,resolution):
        """Constructeur pour la vision d'un robot
         nb : nb images
         fps: nb images par seconde
         resolution : resolution de la caméra"""
        self._thread_image = None
        self.size = resolution
        self.nb_image = nb
        self.balise = False

    def mask(self,color_image):
        """ Compare la couleur RGB avec les mask jaune,vert,bleu et rouge"""
        
        lower_yellow = (20,100,100)
        upper_yellow = (40,255,255)
        
        lower_blue = (100,50,50)
        upper_blue = (130,255,255)

        lower_red = (0,50,50)
        upper_red = (10,255,255)

        lower_green = (50,50,50)
        upper_green = (70,255,255)

        r,g,b = color_image
        cpt = 0

        if lower_yellow[0]<=r<=upper_yellow[0] or lower_blue[0]<=r<=upper_blue[0] or lower_green[0]<=r<=upper_green[0] or lower_red[0]<=r<=upper_red[0]:
            cpt +=1
        if lower_yellow[1]<=g<=upper_yellow[1] or lower_blue[1]<=g<=upper_blue[1] or lower_green[1]<=g<=upper_green[1] or lower_red[1]<=g<=upper_red[1]:
            cpt +=1
        if lower_yellow[2]<=r<=upper_yellow[2] or lower_blue[2]<=b<=upper_blue[2] or lower_green[2]<=b<=upper_green[2] or lower_red[2]<=b<=upper_red[2]:
            cpt += 1

        return cpt == 3
    

    def vision(self,image):
        """ Renvoie True si c'est notre balise et False sinon"""

        #j'adapte l'image à ma résolution 
        image.resize(self.size)
        width, height = self.size        
        #je découpe mon image en 4 régions nord-est,sud-est,sud-ouest,nord-ouest
        north_west_image= image.crop((0,0,width,height))
        south_east_image=image.crop((width/2,height/2,width,height))
        north_east_image=image.crop((0,height/2,width/2,height))
        south_west_image = image.crop((0,height/2,width/2,height))
        #je regarde la couleur dominante de chaque region
        #je compare avec chaque région avec les mask du jaune,rouge,bleu et vert
        #si j'ai mes 4 régions qui contient au moins une couleur jaune,rouge,bleu et vert alors c'est ma balise







