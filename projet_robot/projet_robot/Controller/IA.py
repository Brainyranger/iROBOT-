import time
import math
from threading import Thread
from projet_robot.Simulation.Robot import Robot

global WHEEL_DIAMETER 
global WHEEL_BASE_WIDTH   
WHEEL_DIAMETER = 5
WHEEL_BASE_WIDTH= 40

class IA(Thread):

    def __init__(self):
        super(IA,self).__init__()
        self.Status = True
        self.IA_commande = []
        
    def update(self,dt):
        """fais la mise à jour de notre déplacement en ligne droite"""
        if self.IA_commande == []:
            self.stop()
            #robot.set_motor_dps(0,0)
        else:
            for i in range(0,len(self.IA_commande)):
                if self.IA_commande[i].getStatus() == True:
                    self.IA_commande[i].update(dt)
                    return
            self.stop()
                

    def ajout_commandes(self,commande):
        self.IA_commande.append(commande)
        
    def stop(self):
        self.Status = False
        
    def getStatus(self):
        return self.Status

class Avancer:

    def __init__(self,vitesse,distance,robot):
        self.robot = robot
        self.vitesse = vitesse*3800
        self.distance = distance
        self.distance_parcouru = 0
        self.Status = True

    def update(self,dt) :
        if self.distance_parcouru <= self.distance:
            self.robot.set_motor_dps(self.vitesse,self.vitesse)
            self.distance_parcouru += abs((self.robot.getmovex(dt)+self.robot.getmovey(dt)) - (self.robot.x + self.robot.y))
            print("j'ai fini de parcourir "+str(self.distance_parcouru)+" cm")
        else:
            self.distance_parcouru = 0
            self.stop()

    def getStatus(self):
        return self.Status

    def stop(self):
        self.Status = False
			
class Reculer:

    def __init__(self,vitesse,distance,robot):
        self.robot = robot
        self.vitesse = -vitesse*3800
        self.distance = distance
        self.distance_parcouru = 0
        self.Status = True

    def update(self,dt) :
        if self.distance_parcouru <= self.distance:
            self.robot.set_motor_dps(self.vitesse,self.vitesse)
            self.distance_parcouru += abs((self.robot.getmovex(dt)+self.robot.getmovey(dt)) - (self.robot.x + self.robot.y))
            print("j'ai fini de parcourir "+str(self.distance_parcouru)+" cm")
        else:
            self.distance_parcouru = 0
            self.stop()
    
    def getStatus(self):
        return self.Status

    def stop(self):
        self.Status = False

class Tourner:

    def __init__(self,vitesse,angle,dps,robot):
        self.robot = robot
        self.vitesse = vitesse
        self.angle = angle
        self.dps = dps
        self.angle_parcouru = 0
        self.angleInitial = self.robot.getAngleEnDegre()
        self.Status = True

    def update(self,dt):
        if self.angle_parcouru <= self.angle:
            if self.dps == 0:
                self.stop()
            else:
                self.robot.set_motor_dps(self.vitesse,self.vitesse)
                angle = self.dps*dt*math.pi/180
                self.robot.servo_rotate(angle)
                self.angle_parcouru += self.dps*dt
                print("j'ai fini de parcourir "+str(self.angle_parcouru)+" degré")
        else:
            self.angle_parcouru = 0
            self.stop()

    def getStatus(self):
        return self.Status

    def stop(self):
        self.Status = False
        



class Square:

	def	__init__(self,Robot):
		self.IA_cmd = []
		self.robot = Robot
		self.count = 0
		ToutDroit1 = Avancer(0.03,250,self.robot)
		ToutDroit2 = Avancer(0.03,250,self.robot)
		ToutDroit3 = Avancer(0.03,250,self.robot)
		ToutDroit4 = Avancer(0.03,250,self.robot)
		
		TournerDroite1 = Tourner(0,90,30,self.robot)
		TournerDroite2 = Tourner(0,90,30,self.robot)
		TournerDroite3 = Tourner(0,90,30,self.robot)
		TournerDroite4 = Tourner(0,90,30,self.robot)
		self.IA_cmd.append(ToutDroit1)
		self.IA_cmd.append(TournerDroite1)
		self.IA_cmd.append(ToutDroit2)
		self.IA_cmd.append(TournerDroite2)
		self.IA_cmd.append(ToutDroit3)
		self.IA_cmd.append(TournerDroite3)
		self.IA_cmd.append(ToutDroit4)
		self.IA_cmd.append(TournerDroite4)

		
	def	start(self):
	
		ToutDroit1 = Avancer(0.03,250,self.robot)
		ToutDroit2 = Avancer(0.03,250,self.robot)
		ToutDroit3 = Avancer(0.03,250,self.robot)
		ToutDroit4 = Avancer(0.03,250,self.robot)
		
		TournerDroite1 = Tourner(0,90,30,self.robot)
		TournerDroite2 = Tourner(0,90,30,self.robot)
		TournerDroite3 = Tourner(0,90,30,self.robot)
		TournerDroite4 = Tourner(0,90,30,self.robot)
		self.IA_cmd.append(ToutDroit1)
		self.IA_cmd.append(TournerDroite1)
		self.IA_cmd.append(ToutDroit2)
		self.IA_cmd.append(TournerDroite2)
		self.IA_cmd.append(ToutDroit3)
		self.IA_cmd.append(TournerDroite3)
		self.IA_cmd.append(ToutDroit4)
		self.IA_cmd.append(TournerDroite4)
		
		return True
		
			
			 
	def stop(self):
	
		return self.count >= 8
		
	def update(self,dt):
	
		#if not self.start():
			#self.start()
			
			
		for j in range(0,len(self.IA_cmd)):
                	if self.IA_cmd[j].Status == True:
                    		self.IA_cmd[j].update(dt)
                    		return
                	self.count += 1
                    	
                
		if self.stop():
                	self.robot.set_motor_dps(0,0)