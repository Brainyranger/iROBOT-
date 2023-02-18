
import pygame
from pygame.locals import *
import sys
from projet_robot.Simulation.Environnement import Environnement 
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
        rotated = pygame.transform.rotozoom(IMAGE_ROBOT,math.degrees(SIMUL.robot.ANGLE),1)
        recto = rotated.get_rect(center=(SIMUL.robot.POSITION_X,SIMUL.robot.POSITION_Y))
        SCREEN.blit(rotated,recto)
        #draw sensor
        pygame.draw.line(SCREEN,green,((SIMUL.robot.POSITION_X,SIMUL.robot.POSITION_Y),((SIMUL.robot.POSITION_X+SIMUL.senseur.PORTEE*math.cos(SIMUL.robot.ANGLE)),(SIMUL.robot.POSITION_Y-SIMUL.senseur.PORTEE*math.sin(SIMUL.robot.ANGLE))))
        #draw obstacle
        obstacle1 = pygame.Rect(SIMUL.obstacle1.POSITION_X,SIMUL.obstacle1.POSITION_Y,SIMUL.obstacle1.TAILLE_X,SIMUL.obstacle1.TAILLE_Y)
        pygame.draw.rect(SCREEN,colour,obstacle1)
        obstacle2 = pygame.Rect(SIMUL.obstacle2.POSITION_X,SIMUL.obstacle2.POSITION_Y,SIMUL.obstacle2.TAILLE_X,SIMUL.obstacle2.TAILLE_Y)
        pygame.draw.rect(SCREEN,colour,obstacle2)
        obstacle3 = pygame.Rect(SIMUL.obstacle3.POSITION_X,SIMUL.obstacle3.POSITION_Y,SIMUL.obstacle3.TAILLE_X,SIMUL.obstacle3.TAILLE_Y)
        pygame.draw.rect(SCREEN,colour,obstacle3)
        pygame.display.flip()
        clock.tick(50)
          
pygame.QUIT()
sys.exit()

