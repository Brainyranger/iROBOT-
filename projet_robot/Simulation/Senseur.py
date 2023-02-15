import math


class Senseur:

    def __init__(self,portee):
        """ initialise notre capteur"""
        self.portee=portee

    def get_distance(self,newRobot,obstacle_x,obstacle_y):
        """renvoie la distance entre le robot et l'obstacle"""
        return  math.sqrt(((obstacle_x-newRobot.x)**2)+((obstacle_y-newRobot.y)**2))
        
        
 
