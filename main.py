from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Controller.IA import IA,Avancer,Tourner,Avancer_reel
from projet_robot.Simulation.Senseur import Senseur
from projet_robot.Simulation.Robot import Robot
from projet_robot.Controller.Proxy import portee_senseur
from projet_robot.Controller.Robot_Mockup import Robot_Mockup
from projet_robot.Affichage.Simulation_pygame import Simulation_pygame
import time


bord_map_x = 500
bord_map_y = 420
#Initialisation du robot 
robot = Robot(50,300,0)
senseur = Senseur(portee_senseur)
#initialisation de l'environnment
simul = Environnement(bord_map_x,bord_map_y,robot,senseur)
#initialisation de notre affichage
simul_pygame = Simulation_pygame(simul.bord_map_x,simul.bord_map_y)
#énumération des commandes de notre IA

#commandes pour aller tout droit suivant une vitesse et une distance donnée
IA_avance = Avancer(0.03,5,robot)
#commandes pour tourner selon un angle donnée
IA_tourne_gauche = Tourner(90,0.008,robot)
IA_tourne_droit  = Tourner(-90,0.008,robot)
#commandes générique
#IA = IA([IA_avance,IA_tourne_droit,IA_tourne_gauche])
#commandes pour sélectionner par indice quelle IA on veut éxécuteIA = IA.select_commandes(1)

#commandes pour tracer un carré
#IA = IA([IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche])

#commandes vrai robot
#initialisation du vrai robot :
robot_mockup = Robot_Mockup(robot)
#pour avancer 
IA_avancer_reel = Avancer_reel(0.03,2000,robot_mockup)
IA = IA([IA_avancer_reel])


#initialisation du temps avant le début de la simulation
temps = time.time()
#lancer les thread 
simul.start()
simul_pygame.start()
IA.start()

while simul.running :
        temps_reel = time.time() - temps
        temps = time.time()
        IA.update(temps_reel)
        simul.update(temps_reel)
        simul_pygame.event_update(simul)
        simul.running = IA.getStatus()




