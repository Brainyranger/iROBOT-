class IA_avance_led:
    
    def __init__(self,vitesse,robot,distance):
        self.vitesse = vitesse*3800
        self.robot = proxy_simul(robot)
        self.status = True
        self.distance_parcouru = 0
        self.distance = distance
        
    def update(self,dt):
        
        if self.stop():
            self.robot.set_motor_dps(0,0)
            self.status = False
        
        if self.distance_parcouru > self.distance/2:
            self.robot.set_led()
            time.sleep(0.1)
        
        self.avancer()   
        self.distance_parcouru += self.robot.get_distance_parcourue()
        
    
         	
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
    
  
    def avancer(self):
        self.robot.set_motor_dps(self.vitesse,self.vitesse)

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
             self.cmd_1.update(dt)
        else:
             self.cmd_2.update(dt)
           
        
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
    
