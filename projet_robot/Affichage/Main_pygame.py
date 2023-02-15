
import pygame
import sys
from Simulation_finale import Simulation_finale 
from Obstacle import Obstacle 
from newRobot import newRobot
from Senseur import Senseur 

# création de l'environnemnt :
pygame.init()
pygame.display.set_caption("Ma simulation")
clock = pygame.time.Clock()
green = (0,255,0)
colour = (0,0,255)
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
        image_robot = pygame.image.load("projet_robot/images.jpg")
        rotated = pygame.transform.rotozoom(image_robot,h,1)
        rect = rotated.get_rect(center=(x,y))
        screen.blit(rotated,rect)
        #draw sensor
        for obstacle in simul.list_obs:
            pygame.draw.line(screen,green,obstacle,(simul.robot.x,simul.robot.y))
        #draw obstacle
        simul.obstacle2 = pygame.Rect(simul.obstacle1.x,simul.obstacle1.y,simul.obstacle1.taille_x,simul.obstacle1.taille_y)
        pygame.draw.rect(screen,colour,simul.obstacle2)
        simul.obstacle2 = pygame.Rect(simul.obstacle2.x,simul.obstacle2.y,simul.obstacle2.taille_x,simul.obstacle2.taille_y)
        pygame.draw.rect(screen,colour,simul.obstacle2)
        simul.obstacle3 = pygame.Rect(simul.obstacle3.x,simul.obstacle3.y,simul.obstacle3.taille_x,simul.obstacle3.taille_y)
        pygame.draw.rect(screen,colour,simul.obstacle3)
        pygame.display.flip()
        clock.tick(80)
          
pygame.QUIT()
sys.exit()

