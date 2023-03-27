
import random,math

class Obstacle:
    
    def __init__(self,x,y,taille_x,taille_y,vitesse):
        """ Initialise les coordoonnées, la taille et le nom de nos obstacles """
        self.x = x
        self.y = y
        self.taille_x = taille_x
        self.taille_y = taille_y
        self.vitesse = vitesse*3800
        self.angle = random.uniform(0,math.pi)

    def move(self,list_obs,dt):
        """ Deplace l'obstacle selon x et y en fonction de sa vitesse et de son angle """
        list_obs[0] += list_obs[4]*math.cos(list_obs[5])*dt
        list_obs[1] -= list_obs[4]*math.sin(list_obs[5])*dt

    

            
              