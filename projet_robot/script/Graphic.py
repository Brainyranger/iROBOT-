import pygame
import math

        
class Graphics:
    def __init__(self,x,y)-> None:
        self.robot = pygame.image.load("/home/david/iROBOT-/projet_robot/script/images.jpg") 
        self.rect = self.robot.get_rect(x=x,y=y)
        self.speed = 5
        self.velocity = [0,0]
        self.obstacle = pygame.image.load("/home/david/iROBOT-/projet_robot/script/style-realiste-bombe-noire-ronde.jpg")
    
    def move(self):  
        self.rect.move_ip(self.velocity[0]*self.speed,self.velocity[1]*self.speed) 
          
    def draw_robot(self,screen):
        screen.blit(self.robot,self.rect)
    
    def draw_obstacle(self,screen,x,y):
        self.rect_obs = self.obstacle.get_rect(x=x,y=y)
        screen.blit(self.obstacle,self.rect_obs)
        

        
