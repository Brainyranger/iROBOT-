from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Controller.IA import IA
import pygame

pygame.init()
pygame.display.set_caption("Ma simulation")
bord_map_x = 500
bord_map_y = 420
simul = Environnement(bord_map_x,bord_map_y)
IA_robot = IA(0.2,10,simul.robot)
while simul.running :
        simul.update()
        simul.simul_pygame.event_update(simul)
        IA_robot.update(0.01)

pygame.QUIT()
sys.exit()
