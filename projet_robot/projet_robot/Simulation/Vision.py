from PIL import Image
import numpy as np
import cv2
from projet_robot.Controller.Constante import chemin_images_simulation,chemin_images_reel

class Vision:

    def __init__(self,resolution):
        """Constructeur pour la vision d'un robot
         nb : nb images
         fps: nb images par seconde
         resolution : resolution de la caméra"""
        self.size = resolution
        self.cpt = 0

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
        #en fonction des couleurs rajouter +1 pour le rouge +2 pour le vert +3 pour le bleu et +4 pour le jaune
        cpt = 0
        #on teste pour r
        if lower_yellow[0]<=r<=upper_yellow[0]:
            cpt +=4
        if lower_blue[0]<=r<=upper_blue[0]:
            cpt +=1
        if lower_green[0]<=r<=upper_green[0]:
            cpt +=3
        if lower_red[0]<=r<=upper_red[0]:
            cpt +=2
        #on teste pour g
        if lower_yellow[1]<=g<=upper_yellow[1]:
            cpt +=4
        if lower_blue[1]<=g<=upper_blue[1]:
            cpt +=1
        if lower_green[1]<=g<=upper_green[1]:
            cpt +=3
        if lower_red[1]<=g<=upper_red[1]:
            cpt +=2
        #on teste pour b
        if lower_yellow[2]<=b<=upper_yellow[2]:
            cpt +=4
        if lower_blue[2]<=b<=upper_blue[2]:
            cpt +=1
        if lower_green[2]<=b<=upper_green[2]: 
            cpt +=3
        if lower_red[2]<=b<=upper_red[2]:
            cpt += 2

        #on a du jaune
        if cpt == 12:
            self.cpt += 4
            return True
        
        #on a du vert
        if cpt == 9:
            self.cpt += 3
            return True
        
        #on a du rouge
        if cpt == 6:
            self.cpt += 2
            return True 

        #on a du bleu 
        if cpt == 3:
            self.cpt += 1
            return True
         
    

    def get_balise(self,image):
        """ Renvoie True si c'est notre balise et False sinon"""

        #j'adapte l'image à ma résolution 
        #image.resize(self.size)
        width, height = self.size        
        #je découpe mon image en 4 régions nord-est,sud-est,sud-ouest,nord-ouest
        north_west_image= image.crop((0,0,width,height))
        south_east_image=image.crop((width/2,height/2,width,height))
        north_east_image=image.crop((0,height/2,width/2,height))
        south_west_image = image.crop((0,height/2,width/2,height))
        #je regarde la couleur dominante de chaque region
        
        rgb_seast = self.dominant_color(south_east_image)
        rgb_neast = self.dominant_color(north_east_image)
        rgb_nwest = self.dominant_color(north_west_image)
        rgb_swest = self.dominant_color(south_west_image)
        
        #je compare chaque région avec les mask du jaune,rouge,bleu et vert
        #si j'ai mes 4 régions qui contient au moins une couleur jaune,rouge,bleu et vert alors c'est ma balise
        if self.mask(rgb_seast) == True and self.mask(rgb_swest) and self.mask(rgb_nwest) == True and self.mask(rgb_neast) == True:
            #pour reconnaitre exactement les 4 couleurs de la balise
            return self.cpt == 10 



    def dominant_color(self,image):
        """Renvoie la couleur dominant en triplet rgb"""

        rgb_img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

        hist_r = cv2.calcHist([rgb_img],[0],None,[255],[0,255])
        hist_g = cv2.calcHist([rgb_img],[1],None,[255],[0,255])
        hist_b = cv2.calcHist([rgb_img],[2],None,[255],[0,255])

        max_val_r = np.argmax(hist_r)
        max_val_g = np.argmax(hist_g)
        max_val_b = np.argmax(hist_b)

        return (max_val_r,max_val_g,max_val_b)


