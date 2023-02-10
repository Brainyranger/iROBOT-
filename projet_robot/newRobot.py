import pygame
import math


    
class newRobot:
    
    def __init__(self,x,y,orientation,speed,largeur,bord_map_x,bord_map_y) -> None: 
            self.conversion=3800 #metre en pixel
            self.x = x
            self.y = y
            self.h = orientation
            self.l=largeur #largeur du robot
            self.vl=0.05*self.conversion  #roue gauche
            self.vr=0.05*self.conversion  #roue droite
            self.vitesse_max = speed
            self.bord_map_x = bord_map_x
            self.bord_map_y = bord_map_y
        
    def move_2(self,dt):
        self.x += ((self.vl+self.vr)/2)*math.cos(self.h)*dt
        self.y -= ((self.vl+self.vr)/2)*math.sin(self.h)*dt
        self.h += (self.vr-self.vl)/self.l*dt
        if self.x>=self.bord_map_x :
            self.h += 1
            self.vl=-self.vl
            self.vr=-self.vr
        if self.x<=0 :
            self.h += 30
            self.vl=-self.vl
            self.vr=-self.vr
        if self.y>=self.bord_map_y :
            self.h += 30
            self.vl=-self.vl
            self.vr=-self.vr
        if self.y<=0 :
            self.h += 30
            self.vl=-self.vl
            self.vr=-self.vr    

    def draw_robot(self,x,y,h,screen):
        """affiche le robot"""
        image_robot = pygame.image.load("images.jpg")
        rotated = pygame.transform.rotozoom(image_robot,h,1)
        rect = rotated.get_rect(center=(x,y))
        screen.blit(rotated,rect)