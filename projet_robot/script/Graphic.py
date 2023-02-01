import pygame
import math

        
class Graphic:
    def __init__(self,x,y)-> None:
        """inissialise le robot"""
        self.robot = pygame.image.load("images.jpg") 
        self.rect = self.robot.get_rect(x=x,y=y)
        self.speed = 5
        self.velocity = [0,0]
        self.obstacle = pygame.image.load("style-realiste-bombe-noire-ronde.jpg")
    
    def move(self): 
        """ deplacer le robot"""        
        self.rect.move_ip(self.velocity[0]*self.speed,self.velocity[1]*self.speed) 
          
    def draw_robot(self,screen):
        """affiche le robot"""
        screen.blit(self.robot,self.rect)
    
    def draw_obstacle(self,screen,x,y):
        """affiche les obstacles"""        
        self.rect_obs = self.obstacle.get_rect((x,y))
        screen.blit(self.obstacle,self.rect_obs)
        

        
