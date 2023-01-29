from math import *
import numpy as np
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def norm(self):
        return sqrt(self.x**2 + self.y**2)
    def rotation_vecteur(self,angle):
        Vx = (self.x * math.cos(angle)) - (self.y * math.sin(angle))
        vy = (self.x * math.sin(angle)) + (self.y * math.cos(angle))
        self.x = Vx
        self.y = Vy
    def produit_scalaire(self,other):
        return ((self.x * other.x) +(self.y * other.y))
    def produit_vectoriel(self,other):
        pX = self.x * other.y
        pY = self.y * other.x
        return Vecteur(pX,pY)
    def derivation_vecteur(self,time):
        dxdt = np.diff(self.x)/ np.mean(np.diff(time))
        dydt = np.diff(self.y)/ np.mean(np.diff(time))
        return Vecteur(dxdt,dxdt)
    def vecteur_acceleration(self,time):
        vecteur_vitesse = self.derivation_vecteur(time)
        vecteur_acceleration = vecteur_vitesse.derivation_vecteur(time)
        return Vecteur(vecteur_acceleration.x,vecteur_acceleration.y)
