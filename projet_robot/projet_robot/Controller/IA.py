import time
import math
from projet_robot.Simulation.Robot import Robot



class IA:

    def __init__(self,IA):
        self.list_action_IA = [IA]
        self.current_action = -1
        self.START = False
        self.STOP = False

    def start(self):
        """lance ma liste d'action"""
        self.START = True
        self.STOP = False

    def stop(self):
        """ Arrete ma liste d'action """ 
        self.list_action.stop()
        self.STOP = True
    

    def run(self):
        """ méthode abstraite qui exécute ma liste_d'action"""
        pass

    def add_action_IA(self,action_IA):
        """ ajoute une action"""
        self.list_action.append(action)

    
    def select_action_IA(self,indice):
        """ selectionne une action par indice """
        if indice < 0 or indice >= len(self.list_action):
            return 

        self.list_action[indice].start()



class IA_avancer (IA):

    def __init__(self,IA,vitesse,distance,robot):
        super.__init__(IA)
        self.distance = distance 
        self.distance_parcouru = 0
        self.vitesse = vitesse
        self.robot = robot

    

    def run(self,robot,vitesse,dt):
        """ avancer sur une ligne droite sur une distance donnée"""
        if self.action.STOP:
            return
        if not self.action.START:
            self.start()

        self.robot.ANGLE = 0

        self.distance_parcouru += math.pi*(WHEEL_DIAMETER)

        if self.distance_parcouru >= self.distance:
            self.action.stop()
            print("j'ai fini de parcourir"+str(self.distance_parcouru))
        
        self.robot.run(vitesse,dt)


