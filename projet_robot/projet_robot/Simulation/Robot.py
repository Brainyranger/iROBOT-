import math



class Robot:
    
    WHEEL_DIAMETER   = 5
    WHEEL_BASE_WIDTH = 40

    def __init__(self,POSITION_X,POSITION_Y,ANGLE) -> None: 
            self.POSITION_X  = POSITION_X
            self.POSITION_Y  = POSITION_Y
            self.ANGLE       = ANGLE
            self.MOTOR_LEFT  = 0.05*3800 
            self.MOTOR_RIGHT = 0.05*3800 
        
    def MOVE(self,dt):
        self.POSITION_X += ((self.MOTOR_LEFT + self.MOTOR_RIGHT)/2)*math.cos(self.ANGLE)*dt
        self.POSITION_Y -= ((self.MOTOR_LEFT + self.MOTOR_RIGHT)/2)*math.sin(self.h)*dt
        self.ANGLE      += (self.MOTOR_LEFT - self.MOTOR_RIGHT)/(self.WHEEL_BASE_WIDTH + 2*WHEEL_DIAMETER)*dt
        #a utiliser dans la classe IA
        if self.POSITION_X>=500 or self.POSITION_X<= 0 or self.POSITION_Y>=420 or self.POSITION_Y<=0 :
            self.POSITION_X -= ((self.MOTOR_LEFT + self.MOTOR_RIGHT)/2)*math.cos(self.ANGLE)*dt
            self.POSITION_Y += ((self.MOTOR_LEFT + self.MOTOR_RIGHT)/2)*math.sin(self.h)*dt
            self.ANGLE      += 30