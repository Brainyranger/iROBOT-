from projet_robot.Controller.Toolbox_IA import Constante
import random,math

class Obstacle:
    
    def __init__(self,x,y,taille_x,taille_y,speed):
        """ Initialise les coordoonnées, la taille et le nom de nos obstacles """
        self.x = x
        self.y = y
        self.taille_x = taille_x
        self.taille_y = taille_y
        self.vitesse = vitesse*3800
        self.angle = random.uniform(0,math.pi)

    def move(self,dt):
        """ Deplace l'obstacle selon x et y en fonction de sa vitesse et de son angle """"
        self.x += self.vitesse*math.cos(self.angle)*dt
        self.y -= self.vitesse*math.cos(self.angle)*dt
    

    
    
        
              