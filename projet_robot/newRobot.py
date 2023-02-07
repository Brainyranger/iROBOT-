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
            self.Vx = 0 # en cm/s
            self.Vy = 0 # en cm/s
            self.vitesse_max = speed
            self.robot = pygame.image.load("/home/david/iROBOT-/projet_robot/images.jpg") #modifier le chemin
            self.rect = self.robot.get_rect(x=x,y=y)
            self.speed = 5
            self.velocity = [0,0]
            
    
    def move(self): 
        """ deplacer le robot"""        
        self.rect.move_ip(self.velocity[0]*self.speed,self.velocity[1]*self.speed) 
        
    def move_2(self,dt):
        self.x += ((self.vl+self.vr)/2)*math.cos(self.h)*dt
        self.y -= ((self.vl+self.vr)/2)*math.sin(self.h)*dt
        self.h += (self.vr-self.vl)/self.l*dt

    def movement_avancer_x(self,vx,vy):
        """ fait avancer le robot """
        self.Vx = vx
        self.Vy = vy
        #Tester avec une exception si la vitesse ne dépasse pas la vitesse max du robot
        self.x += (self.Vx * math.cos(self.h)) - (self.Vy * math.sin(self.h))

    def movement_arriere_x(self,vx,vy):
        """ fait reculer le robot """
        self.Vx = vx
        self.Vy = vy
        #Tester avec une exception si la vitesse ne dépasse pas la vitesse max du robot
        self.x -= (self.Vx * math.cos(self.h)) - (self.Vy * math.sin(self.h))

    def movement_descend_y(self,vx,vy):
        """ fait decendre le robot """
        self.Vx = vx
        self.Vy = vy
        #Tester avec une exception si la vitesse ne dépasse pas la vitesse max du robot
        self.y += (self.Vx * math.sin(self.h)) + (self.Vy * math.cos(self.h))

    def movement_monte_y(self,vx,vy):
        """ fait monter le robot """
        self.Vx = vx
        self.Vy = vy
        #Tester avec une exception si la vitesse ne dépasse pas la vitesse max du robot
        self.y -= (vx * math.sin(self.h)) + (self.Vy * math.cos(self.h))

    def tourner_droite(self):
        """ tourne le robot vers la droite """
        self.h = -90

    def tourner_gauche(self):
        """ tourne le robot vers la gauche """
        self.h = 90  
    
    def draw_robot(self,screen):
        """affiche le robot"""
        screen.blit(self.robot,self.rect)

    def draw_robot2(self,x,y,h,screen):
        """affiche le robot"""
        rotated = pygame.transform.rotozoom(self.robot,math.degrees(h),1)
        rect = rotated.get_rect(center=(x,y))
        screen.blit(rotated,rect)