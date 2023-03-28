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
        

        pygame.init()
        pygame.display.set_caption("Ma simulation")
        
    def event_update(self,simul,robot_reel):
        """ gère les événements de notre affichage graphique"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                simul.running = False
        self.screen.fill("White")
        self.draw_robot(simul.robot_virtuel)
        self.draw_led(robot_reel,simul.robot_virtuel,5,5,20,10)
        self.draw_senseur(simul.robot_virtuel)
        for i in range(0,len(simul.list_obs)):	
            self.draw_obstacle(simul.list_obs[i][0],simul.list_obs[i][1],simul.list_obs[i][2],simul.list_obs[i][3])
        pygame.display.flip()
        self.clock.tick(50)

        
    def draw_robot(self,robot):
        """ Affiche le robot """
        rotated = pygame.transform.rotozoom(self.image_robot,math.degrees(robot.angle),1)
        recto = rotated.get_rect(center=(robot.x,robot.y))
        self.screen.blit(rotated,recto)
    
    def draw_led(self,robot_reel,robot_virtuel,dim_led_x,dim_led_y,pos_y_left,pos_y_right):
        """dessine les deux leds du robot""" 
           
        led_left = pygame.Surface((dim_led_x,dim_led_y))
        led_left.fill(robot_reel.LED_LEFT_EYE)
        led_right = pygame.Surface((dim_led_x,dim_led_y))
        led_right.fill(robot_reel.LED_RIGHT_EYE)
        self.screen.blit(led_left,(robot_virtuel.x+math.cos(robot_virtuel.angle)*dim_led_x,dim_led_y*math.sin(robot_virtuel.angle)+(robot_virtuel.y-pos_y_left)))
        self.screen.blit(led_right,(robot_virtuel.x+math.cos(robot_virtuel.angle)*dim_led_x,dim_led_y*math.sin(robot_virtuel.angle)+(robot_virtuel.y+pos_y_right)))
        
    def draw_senseur(self,robot):
        """ Affiche le senseur """
        pygame.draw.line(self.screen,self.green,(robot.x,robot.y),((robot.x + portee_senseur*5.3 * math.cos(robot.angle)),(robot.y - portee_senseur*5.3 * math.sin(robot.angle))))

    def draw_obstacle(self,x,y,taille_x,taille_y):
        """ Affiche l'obstacle """
        obstacle = pygame.Rect(x,y,taille_x,taille_y)
        pygame.draw.rect(self.screen,self.colour,obstacle)
        
    
    def draw_gemme(self,x,y,rayon,color):
        pygame.draw.circle(self.screen,color,(x,y),rayon)
