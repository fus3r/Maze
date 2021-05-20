from main_2D import *
import numpy as np
from World import *

class Player:

    def __init__(self, world:World):        
        self.pos = (0, 0) #position du Player, initialement 0, 0 le centre de la map
        self.dir = np.array([1, 0])
        self.world=world
        self.render_distance=10
        self.cam_size = 100, 50 #en pixels
        self.cam_scale = 1 #longueur réelle dans le monde de la caméra
        self.cam_dist = .1
        pass

    def generate_image(self):
        '''
        --> matrice nombres [0, 255] #TODO : rajouter couleurs
        '''
        render_image=[[0 for i in range(self.cam_size[0])] for j in range(self.cam_size[1])]
        for i in range(self.cam_size[0]):
            for j in range(self.cam_size[1]):
                for wall in self.world.walls:
                    #mur d'équation ax+by+c=0
                    #rayon d'équation rax+rby+rc=0
                    Ax, Ay, Bx, By = wall[0][0], wall[0][1], wall[1][0], wall[1][1]

                    a, b, c = By-Ay, Bx-Ax, Ay*By-Ax*Ay
                    aa, bb, cc = -self.dir[1], self.dir[0], self.dir[1]*self.pos[0]-self.pos[1]*self.dir[0]
                    p, q = aa*c-a*cc, a*bb-aa*b
                    if q==0:
                        continue
                    inter = (b*p/q+c)/-a, p/q
                    dist=((inter[0]-self.pos[0])**2+(inter[1]-self.pos[1])**2)**.5
                    col = (dist<self.render_distance)*(dist*(min-255)/self.render_distance)#la couleur de ce pixel
                    col=int(col)
                    assert col>=0 and col<2**8, 'HERE'

                    render_image[i, j]=col


         
            

        


