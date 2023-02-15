import math


class Senseur:

    def __init__(self,portee):
        """ initialise notre capteur"""
        self.portee=portee

    def get_distance(self,newRobot,obstacle)->float:
        """renvoie la distance entre le robot et l'obstacle"""
        self.distance = math.sqrt(((obstacle.x-newRobot.x)**2)+((obstacle.y-newRobot.y)**2))*0.026
        return distance
        
 
