from main import robot_reel
from PIL import Image
from projet_robot.Controller.Constante import chemin_images_reel

image = robot_reel.get_image()
image.save(chemin_images_reel+"/image_n°0.jpeg")
