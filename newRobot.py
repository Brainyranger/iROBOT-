import pygame
import math
    
class Robot:
    
    def __init__(self,x,y,orientation,speed) -> None:
            
            self.x = x
            self.y = y
            self.h = orientation
            self.vitesse_max = speed

    def vitesse(x,y,dt):
        vx=(x+1-x)/dt
        vy=(y+1-y)/dt
        vitesse=sqrt((vx**2)+(vy**2)) 