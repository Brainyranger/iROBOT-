from projet_robot.Simulation.Environnement import Environnement
import pygame

pygame.init()
pygame.display.set_caption("Ma simulation")
bord_map_x = 500
bord_map_y = 420
simul = Environnement(bord_map_x,bord_map_y)
while simul.running :
        simul.update()
        simul.simul_pygame.event_update(simul)

pygame.QUIT()
sys.exit()
