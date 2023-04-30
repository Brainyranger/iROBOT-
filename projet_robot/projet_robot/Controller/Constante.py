import math

#partie simulation : 
largeur_robot = 60
diametre_roue = 7
portee_senseur = 30
circonference_robot = math.pi * diametre_roue

#partie réelle : 
WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)
