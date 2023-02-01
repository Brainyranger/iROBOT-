import pygame
import math
from Graphic import *
    
class newRobot:
    
    def __init__(self,x,y,orientation,speed) -> None:
            self.robot = pygame.image.load("/home/david/iROBOT-/projet_robot/script/images.jpg") 
            self.x = x
            self.y = y
            self.h = orientation
            self.Vx = 0
            self.Vy = 0
            self.vitesse_max = speed
            self.rect = self.robot.get_rect(x=x,y=y)
    def movement_avancer_x(self,vx,vy):
        self.Vx = vx
        self.Vy = vy
        #Tester avec une exception si la vitesse ne dépasse pas la vitesse max du robot
        self.x += (self.Vx * math.cos(self.h)) - (self.Vy * math.sin(self.h))

    def movement_arriere_x(self,vx,vy):
        self.Vx = vx
        self.Vy = vy
        #Tester avec une exception si la vitesse ne dépasse pas la vitesse max du robot
        self.x -= (self.Vx * math.cos(self.h)) - (self.Vy * math.sin(self.h))

    def movement_descend_y(self,vx,vy):
        self.Vx = vx
        self.Vy = vy
        #Tester avec une exception si la vitesse ne dépasse pas la vitesse max du robot
        self.y += (self.Vx * math.sin(self.h)) + (self.Vy * math.cos(self.h))

    def movement_monte_y(self,vx,vy):
        self.Vx = vx
        self.Vy = vy
        #Tester avec une exception si la vitesse ne dépasse pas la vitesse max du robot
        self.y -= (vx * math.sin(self.h)) + (self.Vy * math.cos(self.h))

    def tourner_droite(self):
        self.h = -90

    def tourner_gauche(self):
        self.h = 90

    #def move(self, vx, vy):
    #    a = vx
    #    b = vy
    #    if (sqrt(a**2+b**2)>0):
    #        a = vx * self.vitesse_max 
    #        b = vy * self.vitesse_max 
    #    robot.Vx = a
    #    robot.Vy = b
    
    def draw_robot(self,screen):
        screen.blit(self.robot,self.rect)