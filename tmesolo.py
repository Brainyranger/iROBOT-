#Q 1.1
def obstacles_coin(self):
        lr = [] 
        taille_x = random.uniform(20,25)
        taille_y = random.uniform(20,25)
        lr.append([0,0,taille_x,taille_y,0,0])
        lr.append([0,self.bord_map_y-taille_y,taille_x,taille_y,0,0])
        lr.append([self.bord_map_x-taille_x,0,taille_x,taille_y,0,0])
        lr.append([self.bord_map_x-taille_x,self.bord_map_y-taille_y,taille_x,taille_y,0,0])     
        return lr