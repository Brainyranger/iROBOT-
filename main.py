import pygame
import time
import sys
import math
from .simulation import Simulation
from ..Obstacle import *
from ..newRobot import newRobot
from ..Senseur import Senseur

# création de l'environnemnt :
pygame.init()
pygame.display.set_caption("Ma simulation")
screen = pygame.display.set_mode((500, 420),pygame.RESIZABLE)
simul = Simulation(screen)
simul.robot2 = newRobot(100,300,0,5,50)
#fais tourner la simulation
while simul.running:
          simul.event_gestion()
          simul.event_update()
          simul.display()
          simul.clock.tick(30)
          

pygame.QUIT()
sys.exit()