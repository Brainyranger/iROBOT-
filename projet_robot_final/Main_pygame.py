import time
import sys
import math
from Simulation_finale import Simulation_finale
from Obstacle import *
from newRobot import newRobot
from Senseur import Senseur

# création de l'environnemnt :
pygame.init()
pygame.display.set_caption("Ma simulation")
clock = pygame.time.Clock()
bord_map_x = 500
bord_map_y = 420
screen = pygame.display.set_mode((bord_map_x,bord_map_y),pygame.RESIZABLE)
simul = Simulation_finale(bord_map_x,bord_map_y)
#fais tourner la simulation
while simul.running:
        #simul.event_gestion()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              simul.running = False
        simul.event_update()
        #simul.display()
        #draw surface
        screen.fill("White")
        #draw robot
        simul.robot.draw_robot(simul.robot.x,simul.robot.y,simul.robot.h,screen)
        #draw sensor
        simul.senseur.draw_sensor(simul.robot,simul.list_obs,screen)
        #draw obstacle
        simul.obstacle1.draw_obstacle(screen)
        simul.obstacle2.draw_obstacle(screen)
        simul.obstacle3.draw_obstacle(screen)
        pygame.display.flip()
        clock.tick(80)
          
pygame.QUIT()
sys.exit()