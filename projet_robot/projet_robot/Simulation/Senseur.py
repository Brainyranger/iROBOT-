import math


class Senseur:

    def __init__(self,PORTEE):
        """ initialise notre capteur"""
        self.PORTEE=(int)(PORTEE*5.3)

    def get_distance(self,Robot,Obstacle_x,Obstacle_y):
        """Renvoie la distance entre le robot et l'obstacle si il est dans le champ de vision du senseur"""
        po=self.PORTEE
        while po >= 0:
            if (int)(Robot.POSITION_X+(po*math.cos(Robot.ANGLE))) == obstacle_x and (int)(Robot.POSITION_Y-(po*math.sin(Robot.ANGLE))) == obstacle_y:
                return  (int)(math.sqrt(((obstacle_x-Robot.POSITION_X)**2)+((obstacle_y-Robot.POSITION_Y)**2))*0.026)
            po -= 1
        return "Rien"
        
        
 
