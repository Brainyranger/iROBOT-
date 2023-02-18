import unittest
from projet_robot.Simulation.Robot import Robot


class TestnewRobot(unittest.TestCase):
    
    def setUp(self):
        self.robot = Robot(10,10,60,5,50,200,400)
        
    def pos_X(self):
        self.assertEqual(self.robot.x,10)
        
    def pos_Y(self):
        self.assertEqual(self.robot.y,10)
        
    def Angle(self):
        self.assertEqual(self.robot.h,60)
    
    def vitesse(self):
        self.assertEqual(self.robot.vitesse_max,5)
        
    def Large(self):
        self.assertEqual(self.robot.l,50)
        
    
        
    
if __name__ == "__main__":
    unittest.main()
    
        
        
    