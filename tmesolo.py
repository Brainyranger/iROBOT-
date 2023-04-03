#Q 1.1
#J'ai uniquement modifié le fichier Environnement.py


def obstacles_coin(self):
        lr = [] 
        taille_x = random.uniform(20,25)
        taille_y = random.uniform(20,25)
        lr.append([0,0,taille_x,taille_y,0,0])
        lr.append([0,self.bord_map_y-taille_y,taille_x,taille_y,0,0])
        lr.append([self.bord_map_x-taille_x,0,taille_x,taille_y,0,0])
        lr.append([self.bord_map_x-taille_x,self.bord_map_y-taille_y,taille_x,taille_y,0,0])     
        return lr

#Q 1.2
#J'ai uniquement modifié le fichier Simulation_pygame.py

def draw_obstacle(self,x,y,taille_x,taille_y):
        """ Affiche l'obstacle """
        obstacle = pygame.Rect(x,y,taille_x,taille_y)
        pygame.draw.rect(self.screen,(255, 165, 0),obstacle)

#Q 1.4
#J'ai uniquement modifié le main pour créer un hexagone

IA_avance = Avancer(0.03,3,robot)
IA_tourne_gauche = Tourner(90,0.008,robot)
IA_tourne_droit  = Tourner(-90,0.005,robot)
IA_tourne_gauche_hexagone = Tourner(45,0.005,robot)
IA_tourne_droit_hexagone = Tourner(-45,0.005,robot)
IA = IA([IA_tourne_gauche_hexagone,IA_avance,IA_tourne_droit_hexagone,IA_avance,IA_tourne_droit_hexagone,IA_avance,IA_tourne_droit,IA_avance,IA_tourne_droit_hexagone,IA_avance,IA_tourne_droit_hexagone,IA_avance])