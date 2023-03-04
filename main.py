from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Controller.IA import IA,Avancer,Tourner,Reculer,Square,Triangle
from projet_robot.Affichage.Simulation_pygame import Simulation_pygame
import time


#Recule = Reculer(0.03,200,Simul.robot)
#initialisation de l'environnment
bord_map_x = 500
bord_map_y = 420
Simul = Environnement(bord_map_x,bord_map_y)
#initialisation de notre affichage
Simul_pygame = Simulation_pygame(Simul.bord_map_x,Simul.bord_map_y)
#Commandes pour faire un carré
IA_square = Square(Simul.robot)
#Commandes pour faire un triangle
IA_triangle = Triangle(Simul.robot)
#commandes pour tracer un carré puis un triangle
IA = IA([IA_square,IA_triangle])
temps = time.time()
#lancer les thread 
Simul.start()
Simul_pygame.start()
IA.start()

#commandes pour sélectionner par indice quelle IA on veut éxécuter
IA = IA.select_commandes(1)

while Simul.running :
        temps_reel = time.time() - temps
        temps = time.time()
        IA.step(temps_reel)
        Simul.update(temps_reel)
        Simul_pygame.event_update(Simul)
        Simul.running = IA.getStatus()

pygame.QUIT()
sys.exit()
