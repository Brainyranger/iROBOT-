from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Controller.IA import IA,Avancer,Tourner
from projet_robot.Simulation.Senseur import Senseur
from projet_robot.Simulation.Robot import Robot
from projet_robot.Controller.Proxy import portee_senseur
from projet_robot.Controller.Robot_Mockup import Robot_Mockup
from projet_robot.Affichage.Simulation_pygame import Simulation_pygame
import time


bord_map_x = 500
bord_map_y = 420
#Initialisation du robot virtuel
robot = Robot(50,300,0)
senseur = Senseur(portee_senseur)
#initialisation du robot mockup
robot_mockup = Robot_Mockup()
#initialisation de l'environnment
simul = Environnement(bord_map_x,bord_map_y,robot,senseur)
#initialisation de notre affichage
#simul_pygame = Simulation_pygame(simul.bord_map_x,simul.bord_map_y)
#énumération des commandes de notre IA pour le robot virtuel

#commandes pour aller tout droit suivant une vitesse et une distance donnée
#IA_avance = Avancer(0.03,10,robot,simul)
#commandes pour tourner selon un angle donnée
#IA_tourne_gauche = Tourner(0.008,90,robot,simul)
#IA_tourne_droit  = Tourner(0.008,-90,robot,simul)
#commandes générique
#IA = IA([IA_avance,IA_tourne_droit,IA_tourne_gauche])
#commandes pour sélectionner par indice quelle IA on veut éxécute
#IA = IA.select_commandes(1)
#commandes pour tracer un carré
#IA = IA([IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche])


#énumération des commandes de notre IA pour le robot mockup

IA_avance_mockup = Avancer(0.03,10,robot_mockup)
IA_tourne_droit_mockup = Tourner(0.008,-90,robot_mockup)
IA_tourne_gauche_mockup = Tourner(0.008,90,robot_mockup)
#commandes générique pour le mockup
IA = IA([IA_avance_mockup,IA_tourne_droit_mockup,IA_tourne_gauche_mockup])
#commandes pour sélectionner par indice quelle IA on veut éxécute
IA = IA.select_commandes(0)
#commandes pour tracer un carré avec le mockup
#IA = IA([IA_avance_mockup,IA_tourne_gauche_mockup,IA_avance_mockup,IA_tourne_gauche_mockup,IA_avance_mockup,IA_tourne_gauche_mockup,IA_avance_mockup,IA_tourne_gauche_mockup])



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
        #simul_pygame.event_update(simul)
        simul.running = IA.getStatus()




