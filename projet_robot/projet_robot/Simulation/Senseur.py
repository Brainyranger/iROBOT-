import math


class Senseur:

    def __init__(self,PORTEE):
        """ initialise notre capteur"""
        self.PORTEE=(int)(PORTEE*5.3)

    def get_distance(self,Robot,Obstacle_x,Obstacle_y):
        """Renvoie la distance entre le robot et l'obstacle si il est dans le champ de vision du senseur"""
        po=self.PORTEE
        while po >= 0:
            if (int)(Robot.x+(po*math.cos(Robot.h))) == obstacle_x and (int)(Robot.y-(po*math.sin(Robot.h))) == obstacle_y:
                return  (int)(math.sqrt(((obstacle_x-Robot.x)**2)+((obstacle_y-Robot.y)**2))*0.026)
            po -= 1
        return "Rien"
        
        
 
