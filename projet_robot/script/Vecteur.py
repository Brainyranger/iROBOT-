import math
import numpy as np
class Vecteur:
    def __init__(self, x, y):
        """ inisialise le vecteurs """
        self.x = x
        self.y = y
    def norm(self):
        """ permet d'avoir la norme du vecteurs """
        return math.sqrt(self.x**2 + self.y**2)
    def rotation_vecteur(self,angle):
        Vx = (self.x * math.cos(angle)) - (self.y * math.sin(angle))
        vy = (self.x * math.sin(angle)) + (self.y * math.cos(angle))
        self.x = Vx
        self.y = vy
    def produit_scalaire(self,other):
        """ fait le produit scalaire de deux vecteurs """
        return ((self.x * other.x) +(self.y * other.y))
    def produit_vectoriel(self,other):
        pX = (self.x * other.x)+(self.x * other.y)
        pY = (self.y * other.x)+(self.y * other.y)
        print(pX,pY)
        return Vecteur(pX,pY)
    def derivation_vecteur(self,time):
        """ derive le vecteur par aport au temps """
        dxdt = np.diff(self.x)/ np.mean(np.diff(time))
        dydt = np.diff(self.y)/ np.mean(np.diff(time))
        print(dxdt,dxdt)
        return Vecteur(dxdt,dxdt)
    def vecteur_acceleration(self,time):
        """ permet d'obtenir l'aceleration du vecteur """
        vecteur_vitesse = self.derivation_vecteur(time)
        vecteur_acceleration = vecteur_vitesse.derivation_vecteur(time)
        return Vecteur(vecteur_acceleration.x,vecteur_acceleration.y)
