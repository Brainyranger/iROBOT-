from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Controller.IA import IA,Avancer,Tourner,Reculer,Square
from projet_robot.Affichage.Simulation_pygame import Simulation_pygame
import pygame,time

pygame.init()
pygame.display.set_caption("Ma simulation")
bord_map_x = 500
bord_map_y = 420
Simul = Environnement(bord_map_x,bord_map_y)
Simul_pygame = Simulation_pygame(Simul.bord_map_x,Simul.bord_map_y)
#Recule = Reculer(0.03,200,Simul.robot)
IA = IA()
#Commandes pour faire un carré
IA_square = Square(Simul.robot)
temps = time.time()
while Simul.running :
        temps_reel = time.time() - temps
        temps = time.time()
        IA_square.update(temps_reel)
        Simul.update(temps_reel)
        Simul_pygame.event_update(Simul)
        Simul.running = IA.getStatus()

pygame.QUIT()
sys.exit()
