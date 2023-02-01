import pygame
import math

        
class Graphics:
    def __init__(self,x,y)-> None:
<<<<<<< HEAD
        self.robot = pygame.image.load("/home/david/iROBOT-/projet_robot/script/images.jpg") 
=======
        """inissialise le robot"""
        self.robot = pygame.image.load("images.jpg") 
>>>>>>> 1dee9f6ed146efd1eb070689f70da4638e8a7b65
        self.rect = self.robot.get_rect(x=x,y=y)
        self.speed = 5
        self.velocity = [0,0]
        self.obstacle = pygame.image.load("/home/david/iROBOT-/projet_robot/script/style-realiste-bombe-noire-ronde.jpg")
    
    def move(self): 
        """ deplacer le robot"""        
        self.rect.move_ip(self.velocity[0]*self.speed,self.velocity[1]*self.speed) 
          
    def draw_robot(self,screen):
        """affiche le robot"""
        screen.blit(self.robot,self.rect)
    
    def draw_obstacle(self,screen,x,y):
<<<<<<< HEAD
        self.rect_obs = self.obstacle.get_rect(x=x,y=y)
=======
        """affiche les obstacles"""        
        self.rect_obs = self.obstacle.get_rect((x,y))
>>>>>>> 1dee9f6ed146efd1eb070689f70da4638e8a7b65
        screen.blit(self.obstacle,self.rect_obs)
        

        
