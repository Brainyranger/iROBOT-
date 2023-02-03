import pygame
from Obstacle import *
from newRobot import *
        
class Simulation:
    
    def __init__(self,surface_map)-> None:
        self.surface_map = surface_map
        self.running = True
        self.clock = pygame.time.Clock()
        self.robot =  newRobot(0,0,0,0)
        self.robot2 = newRobot(50,300,0,0)
        self.obstacle1 = Obstacle(200,300)
        self.obstacle2 = Obstacle(100,80)
        self.obstacle3 = Obstacle(400,200)
    
            
    def event_gestion(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.robot.velocity[0] = -1
        elif keys[pygame.K_RIGHT]:
            self.robot.velocity[0] = 1 
        else:
            self.robot.velocity[0] = 0
            
        if keys[pygame.K_UP]:
            self.robot.velocity[1] = -1
        elif keys[pygame.K_DOWN]:
            self.robot.velocity[1] = 1 
        else:
            self.robot.velocity[1] = 0
                   

    def event_update(self):
        self.robot.move()
            
    
    def display(self):
        self.surface_map.fill("White")
        self.robot.draw_robot(self.surface_map)
        self.robot2.draw_robot(self.surface_map)
        #draw obstacle
        self.obstacle1.draw_obstacle(self.surface_map,200,200)
        self.obstacle2.draw_obstacle(self.surface_map,100,80)
        self.obstacle3.draw_obstacle(self.surface_map,400,200)
        pygame.display.flip()
        
    def run(self):
        while self.running:
            self.event_gestion()
            self.event_update()
            self.display()
            self.clock.tick(10)
            
            