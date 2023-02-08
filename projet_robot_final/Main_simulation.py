import time
import sys
import math
from Simulation_finale import Simulation_finale
from Obstacle import *
from newRobot import newRobot
from Senseur import Senseur

bord_map_x = 500
bord_map_y = 420
simul = Simulation_finale(bord_map_x,bord_map_y)
simul.robot2 = newRobot(100,300,0,5,50,bord_map_x,bord_map_y)
while simul.running :
	simul.event_update()