from main import robot_reel
import time
import PIL
from projet_robot.Controller.Constante import chemin_images_reel

while True:
    robot_reel.start_recording()
    #time.sleep(1)
    image = robot_reel.get_image()
    #robot_reel._start_recording()
    PIL.Image.fromarray(image).save(chemin_images_reel+"/image_n°0.png")
