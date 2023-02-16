import math


class Sensor:

    def __init__(self,portee):
        """ initialise notre capteur"""
        self.portee=(int)(portee*5.3)

    def get_distance(self,Robot,obstacle_x,obstacle_y):
        """renvoie la distance entre le robot et l'obstacle"""
        po=self.portee
        while po>=0:
            if (int)(Robot.x+(po*math.cos(Robot.h)))==obstacle_x and (int)(Robot.y-(po*math.sin(Robot.h)))==obstacle_y:
                return  (int)(math.sqrt(((obstacle_x-Robot.x)**2)+((obstacle_y-Robot.y)**2))*0.026)
            po -= 1
        return "Rien"
        
        
 
