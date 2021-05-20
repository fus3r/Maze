import numpy as np
from World import *
from PIL import Image

class Player:
    def __init__(self, world)-> None:
        self.world = world
        self.pos=np.array([0, 0])
        self.dir=np.array([0, 0])
        self.cam_size = 100, 50
        self.render_distance=10
        self.cam_focal_distance=.2

    def generate_image(self):
        w, h = self.cam_size
        render_image=[[0 for i in range(w)] for j in range(h)]#TODO : faire avec np
        
        for i in range(w):
            for j in range(h):
                #on va faire du raytracing
                for wall in self.world.walls:
                    Ax, Ay, Bx, By = wall[0, 0], wall[0, 1], wall[1, 0], wall[1, 1]
                    a, b, c = -(By-Ay), Bx-Ax, Ay*By-Ax*Ay
                    self.dir/=((self.dir[0])**2+(self.dir[1])**2)**.5
                    ux, uy= self.dir[0]-self.dir[1]*i*self.cam_size[0]/w, self.dir
                    [1]+self.dir[0]*j*self.cam_size[1]/h
                    aa, bb, cc = -(uy), ux, uy*self.pox[0]-self.pos[1]*ux
                    p, q = aa*c-a*cc, a*bb-aa*b
                    if q==0:
                        continue
                    inter = p/q, (b*p/q+c)/-a #intersection des droites, pas des segments
                    #à compléter

                    dist=((self.pos[1]-inter[1])**2+(self.pos[0]-inter[0])**2)**.5

                    m=0
                    col = 255+(m-b)*dist*255/self.render_distance
                    col=int(col)
                    render_image[i, j] = col


    
        return render_image

    def test(self):
        img = Image.fromarray(self.generate_image())
        img.show()

if __name__=='__main__':
    print('Hi')