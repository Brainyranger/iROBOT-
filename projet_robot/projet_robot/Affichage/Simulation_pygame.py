import time
import math,pygame
from pygame.locals import *
from threading import Thread
from  projet_robot.Simulation.Robot import Robot
from  projet_robot.Simulation.Obstacle import Obstacle
from  projet_robot.Simulation.Senseur import Senseur

class Simulation_pygame(Thread):

    def __init__(self,bord_map_x,bord_map_y)-> None:
        """ Initialise les éléments de notre simulation"""
        super(Simulation_pygame,self).__init__()
        self.green = (0,255,0)
        self.colour = (0,0,255)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((bord_map_x,bord_map_y))
        self.image_robot = pygame.image.load("projet_robot/projet_robot/Affichage/images.jpg")


        pygame.init()
        pygame.display.set_caption("Ma simulation")
        
    def event_update(self,simul):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                simul.running = False
        self.screen.fill("White")
        self.draw_robot(simul.robot)
        self.draw_senseur(simul.senseur,simul.robot)
        for i in range(0,len(simul.list_obs)):	
            self.draw_obstacle(simul.list_obs[i][0],simul.list_obs[i][1],simul.list_obs[i][2],simul.list_obs[i][3])
        pygame.display.flip()
        self.clock.tick(50)

        
    def draw_robot(self,robot):
        """ Affiche le robot """
        rotated = pygame.transform.rotozoom(self.image_robot,math.degrees(robot.angle),1)
        recto = rotated.get_rect(center=(robot.x,robot.y))
        self.screen.blit(rotated,recto)
        
    def draw_senseur(self,senseur,robot):
        """ Affiche le senseur """
        pygame.draw.line(self.screen,self.green,(robot.x,robot.y),((robot.x + senseur.portee * math.cos(robot.angle)),(robot.y - senseur.portee * math.sin(robot.angle))))

    def draw_obstacle(self,x,y,taille_x,taille_y):
        """ Affiche l'obstacle """
        obstacle = pygame.Rect(x,y,taille_x,taille_y)
        pygame.draw.rect(self.screen,self.colour,obstacle)