from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Controller.IA import IA,Avancer,Tourner
from projet_robot.Affichage.Simulation_pygame import Simulation_pygame
import time



#initialisation de l'environnment
bord_map_x = 500
bord_map_y = 420
simul = Environnement(bord_map_x,bord_map_y)
#initialisation de notre affichage
simul_pygame = Simulation_pygame(simul.bord_map_x,simul.bord_map_y)
#énumération des commandes de notre IA


#commandes pour aller tout droit suivant une vitesse et une distance donnée
IA_avance = Avancer(0.03,6,simul.robot)
#commandes pour tourner selon un angle donnée
IA_tourne_gauche = Tourner(0.03,90,30,simul.robot)
IA_tourne_droit  = Tourner(0.03,270,30,simul.robot)
IA_tourne_triangle = Tourner(0.03,120,30,simul.robot)

#commandes générique
#IA = IA([IA_avance,IA_tourne_droit,IA_tourne_gauche])
#commandes pour sélectionner par indice quelle IA on veut éxécuter
#IA = IA.select_commandes(2)

#commandes pour tracer un carré
IA = IA([IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche])
#commandes pour tracer un triangle
#IA = IA([IA_avance,IA_tourne_triangle,IA_avance,IA_tourne_triangle,IA_avance,IA_tourne_triangle])

#initialisation du temps avant le début de la simulation
temps = time.time()
#lancer les thread 
simul.start()
#simul_pygame.start()
IA.start()

while simul.running :
        temps_reel = time.time() - temps
        temps = time.time()
        IA.update(temps_reel)
        simul.update(temps_reel)
        simul_pygame.event_update(simul)
        simul.running = IA.getStatus()

pygame.QUIT()
sys.exit()
