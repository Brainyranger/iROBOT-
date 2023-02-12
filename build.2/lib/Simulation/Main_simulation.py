from Simulation_finale import *
from newRobot import *


bord_map_x = 500
bord_map_y = 420
simul = Simulation_finale(bord_map_x,bord_map_y)
simul.robot2 = newRobot(100,300,0,5,50,bord_map_x,bord_map_y)
while simul.running :
	simul.event_update()