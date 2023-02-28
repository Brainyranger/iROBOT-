from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Controller.IA import IA,Avancer,Tourner,Reculer
from projet_robot.Affichage.Simulation_pygame import Simulation_pygame
import pygame,time

pygame.init()
pygame.display.set_caption("Ma simulation")
bord_map_x = 500
bord_map_y = 420
Simul = Environnement(bord_map_x,bord_map_y)
Simul_pygame = Simulation_pygame(Simul.bord_map_x,Simul.bord_map_y)
ToutDroit = Avancer(0.03,2000,Simul.robot)
TournerDroite = Tourner(90,30,Simul.robot)
Recule = Reculer(0.03,2000,Simul.robot)
IA = IA()
#IA.ajout_commandes(ToutDroit)
#IA.ajout_commandes(TournerDroite)
IA.ajout_commandes(Recule)
Recule = Reculer(0.03,2000,Simul.robot)
temps = time.time()
Simul.start()
Simul_pygame.start()
IA.start()
while Simul.running :
        temps_reel = time.time() - temps
        temps = time.time()
        IA.update(temps_reel)
        Simul.update(temps_reel)
        Simul_pygame.event_update(Simul)
        Simul.running = IA.getStatus()

pygame.QUIT()
sys.exit()
