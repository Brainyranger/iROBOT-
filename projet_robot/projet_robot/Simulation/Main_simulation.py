from projet_robot.Simulation.Simulation_finale import Environnement
from projet_robot.Simulation.newRobot import Robot


bord_map_x = 500
bord_map_y = 420
simul = Environnement(bord_map_x,bord_map_y)
while simul.running :
	simul.event_update()