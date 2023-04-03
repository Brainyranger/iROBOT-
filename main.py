from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Controller.IA import IA,Avancer,Tourner,IA_avance_led,IA_conditionnelle
from projet_robot.Simulation.Senseur import Senseur
from projet_robot.Simulation.Robot import Robot
from projet_robot.Controller.Proxy import portee_senseur
from projet_robot.Affichage.Simulation_pygame import Simulation_pygame
import time


bord_map_x = 500
bord_map_y = 420
#Initialisation du robot 
robot = Robot(50,200,0)
senseur = Senseur(portee_senseur)
#initialisation de l'environnment
simul = Environnement(bord_map_x,bord_map_y,robot,senseur)
#initialisation de notre affichage
simul_pygame = Simulation_pygame(simul.bord_map_x,simul.bord_map_y)
#énumération des commandes de notre IA
IA_avance = Avancer(0.03,4,robot)
IA_tourne_gauche = Tourner(90,0.008,robot)
IA_tourne_droit  = Tourner(-90,0.005,robot)
IA_tourne_gauche_hexagone = Tourner(45,0.005,robot)
IA_tourne_droit_hexagone = Tourner(-45,0.005,robot)
#IA pour l'hexagone
#IA = IA([IA_tourne_gauche_hexagone,IA_avance,IA_tourne_droit_hexagone,IA_avance,IA_tourne_droit_hexagone,IA_avance,IA_tourne_droit,IA_avance,IA_tourne_droit_hexagone,IA_avance,IA_tourne_droit_hexagone,IA_avance])

#IA pour le 1
#IA = IA([IA_tourne_gauche,IA_avance])

#IA pour le 0
#IA_avance_zero = Avancer (0.03,2,robot)
#IA = IA([IA_tourne_gauche,IA_avance,IA_tourne_droit,IA_avance_zero,IA_tourne_droit,IA_avance,IA_tourne_droit,IA_avance_zero])

#IA pour le dessin 0 et 1
#IA_avance_zero = Avancer (0.03,2,robot)
#IA = IA([IA_tourne_gauche,IA_avance,IA_tourne_droit,IA_avance_zero,IA_tourne_droit,IA_avance,IA_tourne_droit,IA_avance_zero,IA_tourne_droit,IA_tourne_droit,IA_avance,IA_tourne_gauche,IA_avance])

#IA pour le dessin 0 et 1 en boucle
#IA pour le dessin 0 et 1
IA_avance_zero = Avancer (0.03,2,robot)
IA = IA([IA_tourne_gauche,IA_avance,IA_tourne_droit,IA_avance_zero,IA_tourne_droit,IA_avance,IA_tourne_droit,IA_avance_zero,IA_tourne_droit,IA_tourne_droit,IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche,IA_tourne_gauche,IA_avance,IA_tourne_gauche])
#commandes générique
#IA = IA([IA_avance,IA_tourne_droit,IA_tourne_gauche])
#commandes pour sélectionner par indice quelle IA on veut éxécuteIA = IA.select_commandes(1)

#commandes pour tracer un carré
#IA = IA([IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche,IA_avance,IA_tourne_gauche])

#pour avoir une IA conditionnelle
#IA = IA([IA_conditionnelle(IA_tourne_gauche,IA_avance,simul)])

#commande pour avancer avec des leds alternés
#IA = IA_avance_led(0.03,robot,10)



#initialisation du temps avant le début de la simulation
temps = time.time()
#lancer les thread 
simul.start()
simul_pygame.start()
IA.start()

while simul.running :
        temps_reel = time.time() - temps
        temps = time.time()
        #q 2.3
        #if(IA.curr_command==7):
        #        robot.dessin(False)
        #if(IA.curr_command==11):
        #        robot.dessin(True)    
        #print(robot.crayon)
        IA.update(temps_reel)
        simul.update(temps_reel)
        simul_pygame.event_update(simul)
        #q 2.4
        #if(IA.curr_command == len(IA.ia_command)-1):
        #        IA.curr_command == 0
        #        IA.ia_command[IA.curr_command].start()
        #        IA.status = True
        simul.running = IA.getStatus()




