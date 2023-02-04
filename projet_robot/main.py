import pygame
import sys
from simulation import Simulation
from Obstacle import *
from newRobot import newRobot
from Senseur import Senseur

# création de l'environnemnt :
pygame.init()
pygame.display.set_caption("Ma simulation")
screen = pygame.display.set_mode((500, 420))
simul = Simulation(screen)
simul.robot2 = newRobot(100,300,0,5)


while simul.running:
          simul.event_gestion()
          simul.event_update()
          simul.display()
          simul.clock.tick(20)
            
#Senseur.sense_obstacles(Senseur,newRobot=simul.robot,list_obs=simul.list_obs)


pygame.QUIT()
sys.exit()