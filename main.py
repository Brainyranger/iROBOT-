from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Controller.IA import IA,Avancer
from projet_robot.Affichage.Simulation_pygame import Simulation_pygame
import pygame

pygame.init()
pygame.display.set_caption("Ma simulation")
bord_map_x = 500
bord_map_y = 420
Simul = Environnement(bord_map_x,bord_map_y)
Simul_pygame = Simulation_pygame(Simul.bord_map_x,Simul.bord_map_y)
ToutDroit = Avancer(0.03,2000,Simul.robot)
IA = IA()
IA.ajout_commandes(ToutDroit)
while Simul.running :
        IA.update(Simul.robot,Simul.dt)
        Simul.update()
        Simul_pygame.event_update(Simul)
        Simul.running = IA.getstart()

pygame.QUIT()
sys.exit()
