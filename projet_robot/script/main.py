import pygame
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


def run(self):
     while self.running:
            self.event_gestion()
            self.event_update()
            self.display()
            self.clock.tick(10)
simul.run()

pygame.QUIT()
