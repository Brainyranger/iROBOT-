import pygame

class Obstacle:
    #création d'obstacle
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.list_obstacle = []
        self.list_obstacle.append((x,y))
        self.obstacle = pygame.image.load("/home/david/iROBOT-/projet_robot/script/style-realiste-bombe-noire-ronde.jpg")
    
    #affichage d'obstacle
    
    def draw_obstacle(self,screen,x,y):
        
        self.rect_obs = self.obstacle.get_rect(x=x,y=y)
        screen.blit(self.obstacle,self.rect_obs)
        