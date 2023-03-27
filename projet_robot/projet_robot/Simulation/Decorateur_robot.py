from projet_robot.Simulation.Robot import Robot

class Decorateur_robot_reel(Robot)

    def __init__(self,robot)->None:
    	self.robot = robot
	    self.x = 50
	    self.y = 300
	    self.angle  = 0 #conversion degré par seconde en radian par seconde

    def move(self,dt):
        """ Deplace le robot selon x et y et modifie son angle """
        self.x += ((self.robot.motor_left+self.robot.motor_right)/2)*math.cos(self.angle)*dt
        self.y -= ((self.robot.motor_left+self.robot.motor_right)/2)* math.sin(self.angle)*dt
        self.angle += (self.robot.motor_left - self.robot.motor_right) / (largeur_robot + 2*diametre_roue)*dt
   
    def move_angle(self, angle):
        """ Tourne le robot a l'angle en parametre """
        self.angle += angle*math.pi/180
        if self.angle > 2*math.pi:
            self.angle -= 2*math.pi

    def getAngleEnDegre(self):
        """ Renvoie l'angle dur robot en degré"""
        return self.angle*180/math.pi

    def getmovex(self,dt):
        """ Simule le déplacement du robot en x selon un temps dt """
        return ((self.robot.motor_left+self.robot.motor_right)/2)*math.cos(self.angle)*dt

    def getmovey(self,dt):
        """ Simule le déplacement du robot en y selon un temps dt """
        return ((self.robot.motor_left+self.robot.motor_right)/2)*math.sin(self.angle)*dt


class Tourner:

    def __init__(self,vitesse,angle,dps,robot,str):
        """ Constructeur de notre classe Tourner 
        initialisation de la vitesse de nos roues
        initialisation de l'angle qu'on doit parcourir 
        initialisation de la distance à parcourir en degré/s pour parcourir l'angle
        initialisation de notre robot pour lequel on applique la comande"""

        self.robot = turn(robot)
        self.vitesse = vitesse*3800 
        self.angle = angle
        self.dps = dps
        self.angle_parcouru = 0
        self.status = True
        self.str = str

        
    def update(self,dt):
        """ Fais la mise à jour de notre commande """

        	
        	
        if self.stop():
            self.robot.set_motor_dps(0,0)
            self.status = False
            return
        self.angle_parcouru += self.dps*dt
        turn.tourner(self,self.vitesse,self.dps,dt,self.str)
        print("j'ai fini de parcourir "+str(self.angle_parcouru)+" degré")
       
	
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.angle_parcouru = 0
        self.status = True

    def stop(self):
        """ Arrête la commande en cours """

        return self.angle_parcouru > self.angle
    
    def tourner(self,speed,dps,dt,str):
        self.robot.move_angle(self.dps*dt,str)
        self.robot.set_motor_dps(0,0)
        
class IA_conditionnelle:
    
    def __init__(self,command1,command2,condition):
        self.cmd_1 = command1
        self.cmd_2 = command2
        self.condition = condition
        self.condition_arret = False
        self.status = True
        
        
    def update(self,dt):
           
        if self.stop():
            return
            
        if not self.condition.detection_obstacle():
            self.cmd_2.stop()
            return self.cmd_1.update(dt)
        else:
            self.cmd_1.stop()
            return self.cmd_2.update(dt)
           
        
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.status = True
        self.cmd_1.start()
        self.cmd_2.start()  
        self.condition = self.condition.detection_obstacle()
        
    def stop(self):
        """ Arrête la commande en cours """
        
        return self.condition.detection_collision() or self.condition.detection_collision_bord_map_robot()
    

class IA_avance_led:
    
    def __init__(self,vitesse,robot,distance):
        self.vitesse = vitesse*3800
        self.robot = forward(robot)
        self.status = True
        self.distance_parcouru = 0
        self.distance = distance
        
    def update(self,dt):
        
        if self.stop():
            self.robot.set_motor_dps(0,0)
            self.status = False
        
        if self.distance_parcouru > self.distance/2:
            forward.set_led(self)
        
        forward.avancer(self,self.vitesse,dt)   
        self.distance_parcouru += forward.get_distance_parcourue(self,dt)
        
    
         	
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.distance_parcouru = 0
        self.status = True

    def stop(self):
        """ Arret de la commande en cours"""
        return self.distance_parcouru >= self.distance
    
  


class IA_conditionnelle:
    
    def __init__(self,command1,command2,condition):
        self.cmd_1 = command1
        self.cmd_2 = command2
        self.condition = condition
        self.status = True
        
        
    def update(self,dt):
           
        if self.stop():
            return
            
        if not self.condition.detection_obstacle():
            return self.cmd_1.update(dt)
        else:
            return self.cmd_2.update(dt)
           
        
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.status = True
        self.cmd_1.start()
        self.cmd_2.start()  
        self.condition = self.condition.detection_obstacle()
        
    def stop(self):
        """ Arrête la commande en cours """
        
        return self.condition.detection_collision() or self.condition.detection_collision_bord_map_robot()
    

class IA_conditionnelle_List:
    
    def __init__(self,commands,command2,condition):
        self.cmd_1 = commands
        self.cmd_2 = command2
        self.condition = condition
        self.status = True
        
        
    def update(self,dt):
           
        if self.stop():
            return
            
        if not self.condition.detection_obstacle():
            return self.cmd_1[0].update(dt)
        else:
            self.cmd_2.update(dt)
            return self.cmd_1[1].update(dt)
           
        
    def getStatus(self):
        """ Renvoie l'état de la commande """

        return self.status

    def start(self):
        """ Lance la commande """
        self.status = True
        self.cmd_1[0].start()
        self.cmd_1[1].start()
        self.cmd_2.start()  
        self.condition = self.condition.detection_obstacle()
        
    def stop(self):
        """ Arrête la commande en cours """
        
        return self.condition.detection_collision() or self.condition.detection_collision_bord_map_robot()
    