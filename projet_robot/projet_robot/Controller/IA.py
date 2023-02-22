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


    
    def run_forward(self):
        """ avancer sur une ligne droite sur une distance donnée"""
        self.robot.h = 0
        self.robot.motor_left = self.vitesse
        self.robot.motor_right = self.vitesse

           
        
    def update(self,dt):
        if self.distance_parcouru <= self.distance:
            self.distance_parcouru += self.vitesse/360*math.pi*(WHEEL_DIAMETER)*dt
            self.run_forward()

        self.robot.motor_left = 0
        self.robot.motor_right = 0
        print("j'ai fini de parcourir"+str(self.distance_parcouru)+"cm")
        


