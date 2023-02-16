import math


class Senseur:

    def __init__(self,portee):
        """ initialise notre capteur"""
        self.portee=(int)(portee*5.3)

    def get_distance(self,newRobot,obstacle_x,obstacle_y):
        """renvoie la distance entre le robot et l'obstacle"""
        po=self.portee
        while po>=0:
            if (int)(newRobot.x+(po*math.cos(newRobot.h)))==obstacle_x and (int)(newRobot.y-(po*math.sin(newRobot.h)))==obstacle_y:
                return  (int)(math.sqrt(((obstacle_x-newRobot.x)**2)+((obstacle_y-newRobot.y)**2))*0.026)
            po -= 1
        return "Rien"
        
        
 
