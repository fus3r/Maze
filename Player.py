
import numpy as np
from PIL import Image
from utils import *

class Player:
    def __init__(self)-> None:
        self.pos=np.array([0, 0])
        self.dir=np.array([15, 6])
        self.cam_size = 100, 40
        self.render_distance=10
        self.screen_dist=.2
        self.screen_scale=1

        self.height=1.8#en m

    def print_infos(self):
        print('='*10+' PLAYER INFOS '+ '='*10)
        print(f'Position {self.pos}')
        print(f'dir {self.dir}')
        print(f'CAMERA INFOS')
        print()
        
        print(f'cam_size {self.cam_size}')
        print(f'render_distance {self.render_distance}')
        print(f'screen_dist {self.screen_dist}')
        print(f'screen_scale {self.screen_scale}')
    def rotate(self, theta):
        if (0, 0) in self.dir:
            return
        x, y=self.dir
        if x==0:
            self.dir=np.array([np.sin(theta),np.cos(theta)])
            
        alpha=np.arctan(y/x)
        self.dir=np.array([np.sin(alpha+theta),np.cos(alpha+theta)])

    def set_dir_from_angle(self, theta):
        self.dir= np.cos(theta),np. sin(theta)
        self.dir=np.array(self.dir)
    
    def intersection(self, position, direction, segment):
        '''
            Calcule l'intersection entre un segment et un rayon de vecteur directeur direction et passant par position

        '''
        A, B= segment
        P=position
        d=direction
        I=0

        assert sq(d)!=0
        assert sq(A-P)!=0
        assert sq(B-A)!=0
        alpha, theta=angle_between(A-P, d),angle_between(B-A, d)

        if np.sin(alpha)==0:
            return None
        
        I=A+(B-A)/norm(B-A) * norm(A-P)*np.sin(theta)*np.sin(alpha)

        if np.dot(B-A, I-A)<0:
            return None

        return I

    def col(self, distance):
        '''
        Retourne la couleur d'un pixel en fonction de la distance
        '''
        if distance ==None:
            return (0, 0, 0)
        return tuple([int(255*(1-distance/self.render_distance))]*3)

    def seg(self, distance):
        '''
        Return le tuple de coordonnées en y de l'image qui doivent être colorés dans une même couleur

        '''
        
        if distance is None:
            return None
        return self.size[1]*self.screen_dist*(2-self.height)/self.screen_scale/(distance-self.screen_dist), self.size[1]*self.screen_dist*(self.height)/self.screen_scale/(distance-self.screen_dist)

    def generate_image(self, walls):
        background_col=(0, 0, 0)
        wall_col=(255, 255, 255)
        w, h = self.cam_size
        render_image=[[0 for i in range(w)] for j in range(h)]#TODO : faire avec np
        assert (w, h)==(len(render_image[0]), len(render_image))
        c=0
        
        l=[]
        colors=[]
        for i in range(w):
            #on va faire du raytracing
            dist=None
            for wall in walls:
                #Init
                col=0
                #Computing
                A, B = wall[0], wall[1]                 
                s=self.screen_dist
                d=a(self.dir)
                d_=orth(d)
                P=a(self.pos)
                d=d/norm(d)
                d_=d_/norm(d_)

                K=P+s*d+d_*(i-w/2)*self.screen_scale/w
                I=self.intersection(P, K-P, [A, B])
                if I is None:
                    continue
                print(I)
                new_dist=norm(I-P) #norm(I-K) ???
                print(new_dist)

                if dist is None:
                    dist=new_dist
                elif dist<new_dist:
                    dist=new_dist
                
            colors.append(self.col(dist))
            l.append(self.seg(dist))

        assert len(colors)==self.cam_size[0]
        assert len(colors)==len(l)
        for i in range(len(colors)):
            for j in range(l[i][0], l[i][1]+1):
                
                render_image[j][i]=col[i]
            

        print(f"C {c}, {c/w/h}") 
    
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




         
            

        


