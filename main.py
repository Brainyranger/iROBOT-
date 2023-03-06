from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Controller.IA import IA,Avancer,Tourner,Reculer,Square,Triangle,Approche_Mur
from projet_robot.Affichage.Simulation_pygame import Simulation_pygame
import time


#Recule = Reculer(0.03,200,Simul.robot)
#initialisation de l'environnment
bord_map_x = 500
bord_map_y = 420
Simul = Environnement(bord_map_x,bord_map_y)
#initialisation de notre affichage
Simul_pygame = Simulation_pygame(Simul.bord_map_x,Simul.bord_map_y)
#énumération des commandes de notre IA


#commandes pour aller tout droit suivant une vitesse et une distance donnée
IA_avance = Avancer(0.03,8,Simul.robot)
#commandes pour tourner selon un angle donnée 
IA_tourne_gauche = Tourner(0,90,30,Simul.robot)
IA_tourne_droit  = Tourner(0,180,30,Simul.robot)
#Commandes pour faire un carré
IA_square = Square(Simul.robot)
#Commandes pour faire un triangle
IA_triangle = Triangle(Simul.robot)
#commandes pour s'approcher d'un mur le plus près possible horizontalement
IA_Approche_Mur_x = Approche_Mur(0.003,0.03,Simul.bord_map_x,Simul.robot)
# 2 approche pour gérer IA
#première approche
#commandes générique
IA = IA([IA_square,IA_triangle,IA_avance,IA_tourne_droit,IA_Approche_Mur_x,IA_tourne_gauche])
#commandes pour sélectionner par indice quelle IA on veut éxécuter
IA = IA.select_commandes(1)
#deuxième approche 
#IA = IA([])
#ajout des commandes qu'on veut éxécuter
#IA.ajout_commandes([IA_square])

#initialisation du temps avant le début de la simulation
temps = time.time()
#lancer les thread 
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
