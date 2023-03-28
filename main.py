from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Controller.IA import IA,Avancer,Tourner,IA_avance_led
from projet_robot.Simulation.Senseur import projet_robot.Simulation.Senseur
from projet_robot.Simulation.Robot import projet_robot.Simulation.Robot
from projet_robot.Simulation.Proxy import Proxy,portee_senseur
from projet_robot.Affichage.Simulation_pygame import Simulation_pygame
import time


bord_map_x = 500
bord_map_y = 420
#Initialisation du robot réél et virtuel et du senseur
robot_reel = Robot()
robot_virtuel = Proxy(robot_reel)
senseur = Senseur(portee_senseur)
#initialisation de l'environnment
simul = Environnement(bord_map_x,bord_map_y,robot_virtuel,senseur)
#initialisation de notre affichage
simul_pygame = Simulation_pygame(simul.bord_map_x,simul.bord_map_y)
#énumération des commandes de notre IA

#commandes pour aller tout droit suivant une vitesse et une distance donnée
IA_avance = Avancer(0.03,7,robot_reel,simul.robot_virtuel)
#commandes pour tourner selon un angle donnée
IA_tourne_gauche = Tourner(90,30,robot_reel,simul.robot_virtuel)
#IA_tourne_droit  = Tourner(0.03,90,30,simul.robot,"droite")
#IA_tourne_triangle = Tourner(0.03,90,30,simul.robot,"gauche")

#commandes générique
#IA = IA([IA_avance,IA_tourne_droit,IA_tourne_gauche])
#commandes pour sélectionner par indice quelle IA on veut éxécuter
#IA = IA.select_commandes(2)

#commandes pour tracer un carré
IA = IA([IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche])
#commandes pour tracer un triangle
#IA = IA([IA_avance,IA_tourne_triangle,IA_avance,IA_tourne_triangle,IA_avance,IA_tourne_triangle])
#exo 2.1:
#IA_avance_2cm =  Avancer(0.03,2,simul.robot)
#IA_avance_5cm = Avancer(0.03,5,simul.robot)
#IA_tourne_g45 = Tourner(0.03,45,30,simul.robot,"gauche")
#IA_tourne_d45 = Tourner(0.03,45,30,simul.robot,"droite")
#IA = IA([IA_avance_2cm,IA_tourne_g45,IA_avance_5cm,IA_tourne_droit,IA_avance_5cm,IA_tourne_g45,IA_avance_2cm])
#exo 2.2:
#IA_avance_7cm = Avancer(0.03,7,simul.robot)
#IA_exo22 = IA([IA_avance_2cm,IA_tourne_gauche,IA_avance_5cm,IA_tourne_droit,IA_avance_7cm,IA_tourne_droit,IA_avance_5cm,IA_tourne_gauche,IA_avance_2cm])
#exo 2.3:
#demi_tour = Tourner(0.03,360,30,simul.robot,"gauche")
#IA = IA([IA_conditionnelle(IA_avance,IA_tourne_gauche,simul)])
#IA = IA([IA_tourne_gauche])
#exo 1.2
#IA = IA_avance_led(0.03,simul.robot,10)



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
        simul_pygame.event_update(simul,robot_reel)
        simul.running = IA.getStatus()




