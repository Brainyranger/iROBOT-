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
ToutDroit1 = Avancer(0.03,250,Simul.robot)
ToutDroit2 = Avancer(0.03,250,Simul.robot)
ToutDroit3 = Avancer(0.03,250,Simul.robot)
ToutDroit4 = Avancer(0.03,250,Simul.robot)
TournerDroite1 = Tourner(0,90,30,Simul.robot)
TournerDroite2 = Tourner(0,90,30,Simul.robot)
TournerDroite3 = Tourner(0,90,30,Simul.robot)
#Recule = Reculer(0.03,200,Simul.robot)
IA = IA()
#Commandes pour faire un carré
IA.ajout_commandes(ToutDroit1)
IA.ajout_commandes(TournerDroite1)
IA.ajout_commandes(ToutDroit2)
IA.ajout_commandes(TournerDroite2)
IA.ajout_commandes(ToutDroit3)
IA.ajout_commandes(TournerDroite3)
IA.ajout_commandes(ToutDroit4)
temps = time.time()
while Simul.running :
        temps_reel = time.time() - temps
        temps = time.time()
        IA.update(temps_reel)
        Simul.update(temps_reel)
        Simul_pygame.event_update(Simul)
        Simul.running = IA.getStatus()

pygame.QUIT()
sys.exit()
