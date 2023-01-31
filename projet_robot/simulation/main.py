import pygame
from script.newRobot import newRobot
from ..script import SenseurClass
from ..script import simulation
#création de l'environnemnt :                       
pygame.init()           
pygame.display.set_caption("Ma simulation")
screen = pygame.display.set_mode((500,420))
simul = simulation(screen)

def run(self):
    while self.running:
            self.event_gestion()
            self.event_update()
            self.display()
            self.clock.tick(10)

simul.run()

pygame.QUIT()