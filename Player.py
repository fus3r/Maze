
import numpy as np
from PIL import Image
from utils import *
from vecmaths import *

class Player:
    def __init__(self)-> None:
        self.pos=np.array([0, 0, 0]) #Position 3D de Player
        self.dir=np.array([15, 6, 1]) #Direction du regard
        self.cam_size = 100, 40 #DImensions de l'écran en pixels
        self.render_distance=10 #Distance on sen fout pr le moment
        self.screen_dist=.2 #DIstance entre player et écran
        self.screen_scale=1 #

        self.height=1.8 #

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


    def generate_image(self, walls):
        """
            Return une image (colorée) de ce que voit le joueur en fonction de l'ensemble des murs/objets du monde
                walls : une liste d'objets de type Wall


            Return result : une list w X h X 3, les pixels sont codés chacun sur 24 bits soit 3 channels RGB de 256 valeurs possibles
        """
        
        for wall in walls:
            #Projeter tous les points de wall sur l'écran virtuel
            l=[]
            for vertex in wall.vertices:
                l.append()


        return
    
    def col(self, distance):
        '''
        Retourne la couleur d'un pixel en fonction de la distance
        '''
        if distance ==None:
            return (0, 0, 0)
        return tuple([int(255*(1-distance/self.render_distance))]*3)

    def test(self):
        for _ in range(5):
            img=self.generate_image()
            img=Image.fromarray(img, mode='L')
            img=img.resize((800, 600), resample=Image.NEAREST)
            img.show()
            self.rotate(.1)

