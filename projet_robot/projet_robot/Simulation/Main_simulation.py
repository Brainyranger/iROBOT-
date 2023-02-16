from projet_robot.Simulation.Simulation_finale import *
from projet_robot.Simulation.newRobot import *


bord_map_x = 500
bord_map_y = 420
simul = Simulation_finale(bord_map_x,bord_map_y)
while simul.running :
	simul.event_update()