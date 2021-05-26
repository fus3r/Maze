from Player import Player
import random as r
import numpy as np
from Player import Player
import matplotlib.pyplot as plt

class World:
    def __init__(self)->None:
        self.walls=[]
        self.walls.append(np.array([[4, 0], [-1, 10]]))
        self.player=Player()
        
        pass

    def show_image(self):
        image=self.player.generate_image(self.walls)
        self.player.set_dir_from_angle(np.pi/2)
        return image



w=World()
a=np.array

plt.show()
while 1:
    image=w.show_image()
    image=a(image, dtype=np.uint8)
    if plt.waitforbuttonpress():
        print('Image type', type(image), type(image[0]), type(image[0][0]), type(image[0][0][0]))
        plt.imshow(image)
        w.player.pos+=a([1, 0], dtype=np.uint8)
        w.player.print_infos()


