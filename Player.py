from main_2D import *
import numpy as np

class Player:

    def __init__(self, world):        
        self.pos = (0, 0) #position du Player, initialement 0, 0 le centre de la map
        self.dir = np.array([1, 0])
        self.world=world
        self.render_distance=10
        self.cam_size = 100, 50 #en pixels
        self.cam_scale = 3 #longueur réelle dans le monde de la caméra
        self.cam_focal_dist = 1
        pass

    def get_color_from_distance(self, dist):
        M=255 #valeur maximale du pixel

        return M*(1-dist/self.render_distance)
    def generate_image(self):
        '''
        --> matrice nombres [0, 255] #TODO : rajouter couleurs
        '''
        render_image=[[0 for i in range(self.cam_size[0])] for j in range(self.cam_size[1])]
        render_image=np.array(render_image)
        for i in range(self.cam_size[0]):
            for j in range(self.cam_size[1]):
                for wall in self.world.walls:
                    #mur d'équation ax+by+c=0
                    #rayon d'équation rax+rby+rc=0
                    Ax, Ay, Bx, By = wall[0][0], wall[0][1], wall[1][0], wall[1][1]
                    a, b, c = By-Ay, Bx-Ax, Ay*By-Ax*Ay
                    w = self.cam_size[0]
                    norm=((self.dir[0])**2+(self.dir[1])**2)**.5
                    assert norm>0
                    self.dir=self.dir/norm
                    dx, dy = self.pos[0]+self.cam_focal_dist*self.dir[0]-self.dir[1]*(i-w/2)*self.cam_scale/w,     self.pos[1]+self.cam_focal_dist*self.dir[1]+self.dir[0]*(i-w/2)*self.cam_scale/w        
                    aa, bb, cc = -dy, dx, dy*self.pos[0]-dx*self.pos[1]


                    p, q = aa*c-a*cc, a*bb-aa*b
                    if q==0:
                        continue
                    inter = (b*p/q+c)/-a, p/q
                    inter=np.array(inter)
                    dist=((inter[0]-self.pos[0])**2+(inter[1]-self.pos[1])**2)**.5
                    if dist>self.render_distance:
                        continue



                    col = self.get_color_from_distance(dist)#la couleur de ce pixel
                    AB=2
                    if abs(j-self.cam_size[1]/2)>=self.cam_size[1]*AB*self.cam_focal_dist/dist/self.cam_scale:
                        col=0
                        continue



                    if self.dir.dot(inter-self.pos)<0:
                        continue
                    col=int(col)
                    assert col>=0 and col<2**8, f"col={col}"

                    render_image[j][i]=col
        return render_image

    def rotate(self, theta):
        dx, dy = self.dir[0], self.dir[1]
        self.dir[0]=1
        self.dir[1] = -self.dir[0]*np.tan(theta+np.arctan(dx/dy))

    def test(self):
        for _ in range(5):
            img=self.generate_image()
            img=Image.fromarray(img, mode='L')
            img=img.resize((800, 600), resample=Image.NEAREST)
            img.show()
            self.rotate(.1)




         
            

        


