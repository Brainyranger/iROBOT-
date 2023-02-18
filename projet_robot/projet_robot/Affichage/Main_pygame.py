
import pygame
from pygame.locals import *
import sys
from projet_robot.Simulation.Simulation_finale import Environnement 
from projet_robot.Simulation.Obstacle import Obstacle 
from projet_robot.Simulation.Robot import Robot
from projet_robot.Simulation.Senseur import Senseur 

# création de l'environnemnt :
pygame.init()
pygame.display.set_caption("Ma simulation")
clock = pygame.time.Clock()
green = (0,255,0)
colour = (0,0,255)
BORD_MAP_X = 500
BORD_MAP_Y = 420
SCREEN = pygame.display.set_mode((BORD_MAP_X,BORD_MAP_Y))
SIMUL = Environnement(BORD_MAP_X,BORD_MAP_Y)
IMAGE_ROBOT = pygame.image.load("images.jpg")
#fais tourner la simulation
while SIMUL.running:
        #simul.event_gestion()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              SIMUL.running = False
        SIMUL.event_update()
        #SIMUL.display()
        #draw surface
        SCREEN.fill("White")
        #draw robot
        rotated = pygame.transform.rotozoom(IMAGE_ROBOT,math.degrees(SIMUL.robot.h),1)
        recto = rotated.get_rect(center=(SIMUL.robot.x,SIMUL.robot.y))
        SCREEN.blit(rotated,recto)
        #draw sensor
        pygame.draw.line(SCREEN,green,((SIMUL.robot.x+SIMUL.senseur.PORTEE*math.cos(SIMUL.robot.h)),(SIMUL.robot.y-SIMUL.senseur.portee*math.sin(SIMUL.robot.h))),(SIMUL.robot.x,SIMUL.robot.y))
        #draw obstacle
        obstacle1 = pygame.Rect(SIMUL.obstacle1.x,SIMUL.obstacle1.y,SIMUL.obstacle1.taille_x,SIMUL.obstacle1.taille_y)
        pygame.draw.rect(SCREEN,colour,obstacle1)
        obstacle2 = pygame.Rect(SIMUL.obstacle2.x,SIMUL.obstacle2.y,SIMUL.obstacle2.taille_x,SIMUL.obstacle2.taille_y)
        pygame.draw.rect(SCREEN,colour,obstacle2)
        obstacle3 = pygame.Rect(SIMUL.obstacle3.x,SIMUL.obstacle3.y,SIMUL.obstacle3.taille_x,SIMUL.obstacle3.taille_y)
        pygame.draw.rect(SCREEN,colour,obstacle3)
        pygame.display.flip()
        clock.tick(50)
          
pygame.QUIT()
sys.exit()

