import time,math,pygame
from pygame.locals import *
from threading import Thread
from  projet_robot.Simulation.Robot import Robot
from  projet_robot.Simulation.Obstacle import Obstacle
from  projet_robot.Simulation.Senseur import Senseur
from projet_robot.Controller.Proxy import largeur_robot,diametre_roue,portee_senseur

class Simulation_pygame(Thread):

    def __init__(self,bord_map_x,bord_map_y)-> None:
        """ Initialise les éléments de notre simulation"""
        super(Simulation_pygame,self).__init__()
        self.green = (0,255,0)
        self.colour = (0,0,255)
        self.orange = (255,100,0)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((bord_map_x,bord_map_y))
        self.image_robot = pygame.image.load("projet_robot/projet_robot/Affichage/images.jpg")
        self.image_robot2 = pygame.image.load("projet_robot/projet_robot/Affichage/nouveau_robot.jpg")

        pygame.init()
        pygame.display.set_caption("Ma simulation")
        
    def event_update(self,simul):
        """ gère les événements de notre affichage graphique"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                simul.running = False
        self.screen.fill("White")
        self.draw_led(simul.robot,5,5,simul.robot.x,20,10)
        self.draw_robot(simul.robot)
        self.draw_senseur(simul.senseur,simul.robot)
        self.draw_led(simul.robot,5,5,simul.robot.x,20,10)
        for i in range(0,len(simul.list_obs)):	
            self.draw_obstacle(simul.list_obs[i][0],simul.list_obs[i][1],simul.list_obs[i][2],simul.list_obs[i][3])
        pygame.display.flip()
        self.clock.tick(50)

        
    def draw_robot(self,robot):
        """ Affiche le robot """
        rotated = pygame.transform.rotozoom(self.image_robot,math.degrees(robot.angle),1)
        recto = rotated.get_rect(center=(robot.x,robot.y))
        self.screen.blit(rotated,recto)
    
    def draw_led(self,robot,dim_led_x,dim_led_y,pos_x,pos_y_left,pos_y_right):
        """dessine les deux leds du robot""" 
           
        led_left = pygame.Surface((dim_led_x,dim_led_y))
        led_left.fill(robot.LED_LEFT_EYE)
        led_right = pygame.Surface((dim_led_x,dim_led_y))
        led_right.fill(robot.LED_RIGHT_EYE)
        self.screen.blit(led_left,(pos_x+math.cos(robot.angle)*dim_led_x,dim_led_y*math.sin(robot.angle)+(robot.y-pos_y_left)))
        self.screen.blit(led_right,(pos_x+math.cos(robot.angle)*dim_led_x,dim_led_y*math.sin(robot.angle)+(robot.y+pos_y_right)))
        
    def draw_senseur(self,senseur,robot):
        """ Affiche le senseur """
        pygame.draw.line(self.screen,self.green,(robot.x,robot.y),((robot.x + senseur.portee * math.cos(robot.angle)),(robot.y - senseur.portee * math.sin(robot.angle))))

    def draw_obstacle(self,x,y,taille_x,taille_y):
        """ Affiche l'obstacle """
        obstacle = pygame.Rect(x,y,taille_x,taille_y)
        pygame.draw.rect(self.screen,(255, 165, 0),obstacle)