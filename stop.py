from main import robot_reel,Avancer

avance_1 = Avancer(1,1,robot_reel)
avance_1.update(1)
robot_reel.set_motor_dps(robot_reel.MOTOR_LEFT+robot_reel.MOTOR_RIGHT,0)


