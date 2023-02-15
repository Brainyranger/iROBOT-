import unittest
from Obstacle import Obstacle


class TestObstacle(unittest.TestCase):
    def setUp(self):
        self.obs = Obstacle(10,10,"obs_1",20,20)
        
    
    def obs_X(self):
        self.assertEqual(self.obs.x,10)
        
    def obs_Y(self):
        self.assertEqual(self.obs.y,10)
        
    def largeur(self):
        self.assertEqual(self.obs.taille_x,20)
        
    def longueur(self):
        self.assertEqual(self.obs.taille_y,20)
        
    def nom_obs(self):
        self.assertEqual(self.obs.nom,"obs_1")
        
        

if __name__ == "__main__":
    unittest.main()
        