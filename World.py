from Player import Player
import random as r
import numpy as np

class World:

    def __init__(self) -> None:
        self.player = Player(self)      
        self.walls=[np.array([[-5, 10], [10, 3]])]
        self.walls.append(np.array([[-6, -.5], [-10, .5]]))
        self.walls.append(np.array([[-6, -.5], [-10, .5]])+np.array([[1, 3], [1, 3]]))
        self.walls.append(np.array([[-6, -.5], [-10, .5]])+np.array([[-1, 3], [1, 3]]))
        pass






if __name__=='__main__':
    w=World()
    w.player.test()
