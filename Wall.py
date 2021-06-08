import numpy as np

class Wall:


    def __init__(self):
        self.vertices = []
        sin, cos, pi = np.sin, np.cos, np.pi
        for i in range(4):
            self.vertices.append([cos(i*pi/2), sin(i*pi/2), 0])
        
        self.vertices = np.array(self.vertices) + np.array([0, 1, 0])
        return