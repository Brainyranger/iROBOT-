from projet_robot.Simulation.Environnement import Environnement
from projet_robot.Simulation.Robot import Robot


BORD_MAP_X = 500
BORD_MAP_Y = 420
simul = Environnement(BORD_MAP_X,BORD_MAP_Y)
while simul.running :
	simul.event_update()