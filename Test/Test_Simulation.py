import unittest
from projet_robot.Simulation.Robot import Robot
from  projet_robot.Simulation.Obstacle import Obstacle
from projet_robot.Simulation.Senseur import Senseur
from projet_robot.Simulation.Environnement import Environnement

class TestRobot(unittest.TestCase):
    
    def setUp(self):
        self.robot = Robot(10,10,0)
        
    def pos_X(self):
        self.assertEqual(self.robot.x,10)
        
    def pos_Y(self):
        self.assertEqual(self.robot.y,10)
        
    def Angle(self):
        self.assertEqual(self.robot.angle,0)
    
    def vitesse_moteur_left(self):
        self.assertEqual(self.robot.motor_left,0)
        
    def vitesse_moteur_right(self):
        self.assertEqual(self.robot.motor_right,0)

    def test_set_motor(self):
        v_right = self.robot.motor_right
        v_left = self.robot.motor_left
        self.robot.set_motor_dps(10,10)
        self.assertNotEqual(self.robot.motor_left,v_left)
        self.assertNotEqual(self.robot.motor_right,v_right)


    def test_offset_motor_encoder(self):
        self.robot.offset_motor_encoder("self.motor_right+self.motor_left",50)
        self.assertEqual(self.robot.motor_left,50)
        self.assertEqual(self.robot.motor_right,50)

    def test_move_angle(self):
        angle_servo = self.robot.angle
        self.robot.move_angle(90)
        self.assertNotEqual(self.robot.angle,angle_servo)

    def test_move(self):
        x1 = self.robot.x
        y1 = self.robot.y
        self.robot.motor_left = 0.05*3800
        self.robot.motor_right = 0.05*3800
        self.robot.angle = 45
        self.robot.move(0.001)
        self.assertNotEqual(self.robot.x,x1)
        self.assertNotEqual(self.robot.y,y1)


    
        
class TestObstacle(unittest.TestCase):
    def setUp(self):
        self.obs = Obstacle(10,10,20,20,0) 
    
    def obs_X(self):
        self.assertEqual(self.obs.x,10)
        
    def obs_Y(self):
        self.assertEqual(self.obs.y,10)
        
    def obs_largeur(self):
        self.assertEqual(self.obs.taille_x,20)
        
    def obs_longueur(self):
        self.assertEqual(self.obs.taille_y,20)
        
    def obs_vitesse(self):
        self.assertEqual(self.obs.vitesse,0) 

class TestSenseur(unittest.TestCase):
    def setUp(self):
        self.senseur = Senseur(10)
        self.obs = Obstacle(20,10,20,20,0)
        self.robot = Robot(10,10,0)

    def test_portee(self):
        return self.senseur.portee == 10

    def test_getDistance(self):
        distance = self.senseur.get_distance(self.robot,self.obs.x,self.obs.y,self.obs.taille_x,self.obs.taille_y)
        self.assertNotEqual(distance,0)



class TestEnvironnement(unittest.TestCase):
    def setUp(self):
        self.env_robot = Robot(10,10,0)
        self.env_senseur = Senseur(30)
        self.env = Environnement(520,420,self.env_robot,self.env_senseur)
        self.env.list_obs = self.env.generer_obstacles(5,0)

    def test_generer_obs(self):
        self.assertEqual(len(self.env.list_obs),5)
    


 


if __name__ == "__main__":
    unittest.main()
    
        
        
    