from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Controller.IA import IA
import pygame

pygame.init()
pygame.display.set_caption("Ma simulation")
bord_map_x = 500
bord_map_y = 420
simul = Environnement(bord_map_x,bord_map_y)
IA_robot = IA(0.2*3800,200,simul.robot)
while simul.running :
        simul.update()
        IA_robot.update(simul.dt)
        simul.simul_pygame.event_update(simul)
        simul.running = IA_robot.s

pygame.QUIT()
sys.exit()
