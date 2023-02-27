import time
import math
from projet_robot.Simulation.Robot import Robot

global WHEEL_DIAMETER 
global WHEEL_BASE_WIDTH   
WHEEL_DIAMETER = 5
WHEEL_BASE_WIDTH= 40

class IA:

    def __init__(self):
        self.start = True
        self.IA_liste_commandes = []
        
    def update(self,robot,dt):
        """fais la mise à jour de notre déplacement en ligne droite"""
        if self.IA_liste_commandes == []:
            self.stop()
            robot.set_motor_dps(0,0)
        else:
            for i in range(0,len(self.IA_liste_commandes)):
                com = self.IA_liste_commandes[i]
                if com.update(robot):
                    i -= 1
                    com.update(dt)
            self.stop()

    def ajout_commandes(self,commande):
        self.IA_liste_commandes.append(commande)
        
    def stop(self):
        self.start = False
        
    def getstart(self):
        return self.start

class Avancer:

    def __init__(self,vitesse,distance,robot):
        self.robot = robot
        self.vitesse = vitesse*3800
        self.distance = distance
        self.distance_parcouru = 0

    def update(self,dt) :
        if self.distance_parcouru <= self.distance:
            self.robot.set_motor_dps(self.vitesse,self.vitesse)
            self.distance_parcouru += math.sqrt((self.robot.getmovex(dt)+self.robot.x)**2+(self.robot.getmovey(dt) - self.robot.y)**2)
            print("j'ai fini de parcourir "+str(self.distance_parcouru)+" cm")
            return True
        return False
			
class Reculer:

    def __init__(self,vitesse,distance,robot):
        self.robot = robot
        self.vitesse = -vitesse*3800
        self.distance = distance
        self.distance_parcouru = 0

    def update(self,dt) :
        if self.distance_parcouru <= self.distance:
            self.robot.set_motor_dps(self.vitesse,self.vitesse)
            self.distance_parcouru += abs((robot.getmovex(dt)+robot.getmovey(dt)) - (robot.x + robot.y))
            print("j'ai fini de parcourir "+str(self.distance_parcouru)+" cm")
            return True
        return False

class Tourner:

    def __init__(self,vitesse,angle,dps,robot):
        self.robot = robot
        self.vitesse = vitesse
        self.angle = angle
        self.dps = dps
        self.angle_parcouru = 0

    def update(self,dt):
        if abs(self.angle_parcouru) <= abs(self.angle):
            if self.dps > 0:
                self.robot.set_vitesse(self.vitesse + 1,self.vitesse)
            else:
                self.robot.set_vitesse(self.vitesse,self.vitesse + 1)
            self.angle_parcouru += 1
            return True
        return False
        


