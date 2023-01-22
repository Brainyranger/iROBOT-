import pygame
from Robot import Robot
from Graphic import Graphic
DIMENSIONS_MAP = (422,612)
gfx = Graphic(DIMENSIONS_MAP,"little.png","istockphoto-690551082-612x612.jpg")
           
robot = Robot(40,380,0,0.1)


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    robot.movement_avancer_x()
    gfx.map.blit(gfx.map_image,(0,0))
    gfx.draw(robot.x,robot.y,robot.h)
    
   
    pygame.display.flip()
