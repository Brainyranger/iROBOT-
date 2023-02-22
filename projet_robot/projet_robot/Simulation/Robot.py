import math

global WHEEL_DIAMETER 
global WHEEL_BASE_WIDTH   
WHEEL_DIAMETER = 5
WHEEL_BASE_WIDTH= 40

class Robot:
    
  

    def __init__(self,x,y,h) -> None: 
            self.x  = x
            self.y  = y
            self.h  = h
            self.motor_left  = 0.05*3800 
            self.motor_right = 0.05*3800 
        
    def move(self,dt):
        self.x += ((self.motor_left + self.motor_right)/2) * math.cos(self.h)*dt
        self.y -= ((self.motor_left + self.motor_right)/2) * math.sin(self.h)*dt
        self.h += (self.motor_left - self.motor_right) / (WHEEL_BASE_WIDTH + 2*WHEEL_DIAMETER)*dt
        #a utiliser dans la classe IA
        if self.x>=500 or self.x<= 0 or self.y>=420 or self.y<=0 :
            self.x -= ((self.motor_left + self.motor_right)/2) * math.cos(self.h)*dt
            self.y += ((self.motor_left + self.motor_right)/2) * math.sin(self.h)*dt
            self.h += 30