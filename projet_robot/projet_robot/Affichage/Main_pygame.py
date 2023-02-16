
import pygame
import sys
from projet_robot.Simulation import Simulation_finale 
from projet_robot.Simulation.Obstacle import Obstacle 
from projet_robot.Simulation.newRobot import newRobot
from projet_robot.Simulation.Senseur import Senseur 

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
image_robot = pygame.image.load("images.jpg")
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
        rotated = pygame.transform.rotozoom(image_robot,math.degrees(simul.robot.h),1)
        recto = rotated.get_rect(center=(simul.robot.x,simul.robot.y))
        screen.blit(rotated,recto)
        #draw sensor
        pygame.draw.line(screen,green,((simul.robot.x+simul.senseur.portee*math.cos(simul.robot.h)),(simul.robot.y-simul.senseur.portee*math.sin(simul.robot.h))),(simul.robot.x,simul.robot.y))
        #draw obstacle
        obstacle1 = pygame.Rect(simul.obstacle1.x,simul.obstacle1.y,simul.obstacle1.taille_x,simul.obstacle1.taille_y)
        pygame.draw.rect(screen,colour,obstacle1)
        obstacle2 = pygame.Rect(simul.obstacle2.x,simul.obstacle2.y,simul.obstacle2.taille_x,simul.obstacle2.taille_y)
        pygame.draw.rect(screen,colour,obstacle2)
        obstacle3 = pygame.Rect(simul.obstacle3.x,simul.obstacle3.y,simul.obstacle3.taille_x,simul.obstacle3.taille_y)
        pygame.draw.rect(screen,colour,obstacle3)
        pygame.display.flip()
        clock.tick(50)
          
pygame.QUIT()
sys.exit()

