import numpy as np


class World:
    def __init__(self)->None:
        self.walls=[]
        self.walls.append(np.array([[4, 0], [-1, 10]]))
        self.player=Player(self)
        pass

w=World()

def test():
    print("Hello World")