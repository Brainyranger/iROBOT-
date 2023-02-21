import math


class Senseur:

    def __init__(self,portee):
        """ initialise notre capteur"""
        self.portee=(int)(portee*5.3)

    def get_distance(self,Robot,x,y,t_x,t_y):
        """Renvoie la distance entre le robot et l'obstacle si il est dans le champ de vision du senseur"""
        po=self.portee
        while po >= 0:
            if ((int)(Robot.x+(po*math.cos(Robot.h))) >= x and (int)(Robot.y-(po*math.sin(Robot.h))) >= y) and ((int)(Robot.x+(po*math.cos(Robot.h))) <= (x+t_x) and (int)(Robot.y-(po*math.sin(Robot.h))) <= (y+t_y)):
                return  (int)(math.sqrt(((x-Robot.x)**2)+((y-Robot.y)**2))*0.026)
            po -= 1
        return "Rien"
        
        
        
 
