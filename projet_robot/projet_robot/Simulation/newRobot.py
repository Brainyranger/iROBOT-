import math



class newRobot:
    
    def __init__(self,x,y,orientation,largeur) -> None: 
            self.x = x
            self.y = y
            self.h = orientation
            self.l=largeur #largeur du robot
            self.vl=0.05*3800 #roue gauche
            self.vr=0.05*3800 #roue droite
        
    def move(self,dt):
        self.x += ((self.vl+self.vr)/2)*math.cos(self.h)*dt
        self.y -= ((self.vl+self.vr)/2)*math.sin(self.h)*dt
        self.h += (self.vr-self.vl)/self.l*dt
        #a utiliser dans la classe IA
        if self.x>=500 or self.x<= 0 or self.y>=420 or self.y<=0 :
            self.x -= ((self.vl+self.vr)/2)*math.cos(self.h)*dt
            self.y += ((self.vl+self.vr)/2)*math.sin(self.h)*dt
            self.h +=30