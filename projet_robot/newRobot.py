import pygame
import math
from Senseur import *

    
class newRobot:
    
    def __init__(self,x,y,orientation,speed,largeur) -> None: 
            self.conversion=3800 #metre en pixel
            self.x = x
            self.y = y
            self.h = orientation
            self.l=largeur #largeur du robot
            self.vl=0.01*self.conversion  #roue gauche
            self.vr=0.01*self.conversion  #roue droite
            self.vitesse_max = speed
            self.robot = pygame.image.load("/home/david/iROBOT-/projet_robot/images.jpg") #modifier le chemin
            self.rect = self.robot.get_rect(x=x,y=y)
            self.speed = 5
            self.velocity = [0,0]
            self.map_width, self.map_height= pygame.display.get_surface().get_size()
            
    
    def move(self): 
        """ deplacer le robot"""        
        self.rect.move_ip(self.velocity[0]*self.speed,self.velocity[1]*self.speed) 
        
    def move_2(self,dt):
        self.x += ((self.vl+self.vr)/2)*math.cos(self.h)*dt
        self.y -= ((self.vl+self.vr)/2)*math.sin(self.h)*dt
        self.h += (self.vr-self.vl)/self.l*dt
        if self.x>=self.map_width :
            self.vl=-self.vl
            self.vr=-self.vr
        if self.x<=0 :
            self.vl=-self.vl
            self.vr=-self.vr
        if self.y>=self.map_heigth :
            self.vl=-self.vl
            self.vr=-self.vr
        if self.y<=0 :
            self.vl=-self.vl
            self.vr=-self.vr

    def movement_avancer_x(self,dt):
        """ fait avancer le robot """
        self.x += ((self.vl+self.vr)/2)*math.cos(self.h)*dt

    def movement_arriere_x(self,dt):
        """ fait reculer le robot """
        self.x -= ((self.vl+self.vr)/2)*math.cos(self.h)*dt

    def movement_descend_y(self,dt):
        """ fait decendre le robot """
        self.y += ((self.vl+self.vr)/2)*math.sin(self.h)*dt

    def movement_monte_y(self,dt):
        """ fait monter le robot """
        self.y -= ((self.vl+self.vr)/2)*math.sin(self.h)*dt

    def tourner_droite(self):
        """ tourne le robot vers la droite """
        self.h -= 90

    def tourner_gauche(self):
        """ tourne le robot vers la gauche """
        self.h += 90
    
    def draw_robot(self,screen):
        """affiche le robot"""
        screen.blit(self.robot,self.rect)

    def draw_robot2(self,x,y,h,screen):
        """affiche le robot"""
        rotated = pygame.transform.rotozoom(self.robot,math.degrees(h),1)
        rect = rotated.get_rect(center=(x,y))
        screen.blit(rotated,rect)