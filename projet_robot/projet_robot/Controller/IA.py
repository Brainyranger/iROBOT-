import time
import math
from projet_robot.Simulation.Robot import Robot

global WHEEL_DIAMETER 
global WHEEL_BASE_WIDTH   
WHEEL_DIAMETER = 5
WHEEL_BASE_WIDTH= 40

class IA:

    def __init__(self,vitesse,distance,robot):
        self.distance = distance 
        self.distance_parcouru = 0
        self.vitesse = vitesse
        self.robot = robot
        self.s = True
(s
    
    def run_forward(self,dt):
        """ avancer sur une ligne droite sur une distance donnée"""
        self.robot.h = 0
        self.robot.motor_left = self.vitesse
        self.robot.motor_right = self.vitesse
        self.robot.move(dt)
        

           
        
    def update(self,dt):
        """fais la mise à jour de notre déplacement en ligne droite"""
        if self.distance_parcouru <= self.distance:
            x=self.robot.x
            y=self.robot.y
            #self.distance_parcouru += (self.vitesse/((WHEEL_DIAMETER)//2))*dt
            self.run_forward(dt)
            self.distance_parcouru += (int)((self.robot.x+self.robot.y) - (x+y))
        else:
            self.s = False
        self.robot.motor_left = 0
        self.robot.motor_right = 0
        print("j'ai fini de parcourir "+str(self.distance_parcouru)+" cm")
        


