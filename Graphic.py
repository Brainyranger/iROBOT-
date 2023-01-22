
import pygame
import math

        
class Graphic:
    def __init__(self,dimension,image_path,map)-> None:
        pygame.init()
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.green = (0,255,0)
        self.blue  = (0,0,255)
        self.red   = (255,0,0)
        self.yel   = (255,255,0)
        
        self.robot = pygame.image.load(image_path)
        self.map_image = pygame.image.load(map)
        
        self.height,self.width = dimension
        
        pygame.display.set_caption("Ma simulation")
        self.map = pygame.display.set_mode(((self.width,self.height)))
        self.map.blit(self.map_image,(0,0))
        
    def draw(self,x,y,h):
        bot = pygame.transform.rotozoom(self.robot,math.degrees(h),1)
        rebot = bot.get_rect(center=(x,y))
        self.map.blit(bot,rebot)
        
