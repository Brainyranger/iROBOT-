import unittest
from projet_robot.Simulation.Senseur import Senseur
from projet_robot.Simulation.Robot import Robot

class TestSenseur(unittest.TestCase):
    def setUp(self):
        self.senseur = Senseur(10)

    def test_portee(self):
        return self.senseur.PORTEE == 10

 


if __name__ == "__main__":
    unittest.main()