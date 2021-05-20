from utils import *
from PIL import Image
import numpy as np
import pygame as pg
import pygame.freetype as freetype

class Ascii2D:

    GRADIENTS = Constants.GRADIENTS
    HEIGHT = Constants.HEIGHT
    WIDTH = Constants.WIDTH

    def rvb(self,color:int, mode=0):
        """Returns symbol using color code given by image.getpixel

        Args:
            color (int): color code

        Returns:
            symbol (str): Symbol
        """
        ind=color*(len(self.GRADIENTS)-1)/255
        if mode==1:
            assert color!=1 or color!=0, f"color = {color}"
            ind=color*(len(self.GRADIENTS)-1)
            assert ind==int(ind), "RVB mode problem"
        assert ind<=len(self.GRADIENTS)-1, "trhythdrtjx"
        symbol = self.GRADIENTS[int(ind)]
        return symbol


    def pic_to_matrix2(self,longueur:int,largeur:int,filename:str,ext:str):
        image = Image.open(f'img/{filename}.{ext}')
        image = image.convert('1')
        image.save(f'img/{filename}_black.{ext}')
        image = Image.open(f'img/{filename}_black.{ext}')
        
        long,larg = image.size
        long,larg=list(np.linspace(0, long, longueur,dtype=int)),list(np.linspace(0, larg, largeur,dtype=int))
        del long[-1]
        del larg[-1]

        matrix = []
        lst = []
        for indexColor_largeur in larg:
            for indexColor_longueur in long:
                color = image.getpixel((int(indexColor_longueur),int(indexColor_largeur)))
                lst.append(color)
            matrix.append(lst)
            lst=[]

        return matrix

    def pic_to_matrix(self,longueur:int,largeur:int,filename:str,ext:str):
        image = Image.open(f'img/{filename}.{ext}')
        image = image.convert('1')
        image.save(f'img/{filename}_black.{ext}')
        image = Image.open(f'img/{filename}_black.{ext}')

        return np.asarray(image.resize((longueur, largeur), resample=2))

    def pic_to_matrix3(self,longueur:int,largeur:int,image):
        return np.asarray(image.resize((longueur, largeur), resample=2))


    def transform(self,matrix:list, mode=0):
        """Transform image (any extension) to ASCII Art

        Args:
            longueur (int): Length desired
            largeur (int): Width desired
            filename (str): Filename
            ext (str): Filename extension
            mode (int): type d'encodage de pixels
                0: [0;255]
                1: [|0, 1|]

        Returns:
            None:
        """

        h, w = len(matrix), len(matrix[0])
        res=['' for j in range(h)] #TODO creer avec np
        #assert (longueur<long and largeur<larg), "Invalid width or length"

        #modified = [[0]*longueur for _ in range(largeur)]
        if mode==1:
            coef=255
        
        for j in range(h):
            for i in range(w):
                res[j] += self.rvb(self, matrix[j][i], mode=mode)
        return res

    def display_image(slef, image):
        assert type(int(image.mode))==int
        matrix = Ascii2D.pic_to_matrix3(Ascii2D,200, 200, image)
        modified_matrix = Ascii2D.transform(Ascii2D,matrix, mode=int(image.mode))
        Ascii2D.display(Ascii2D,modified_matrix)
        
    def display(self,modified_matrix):
        """for i in modified_matrix:
            print("".join([str(k) for k in i]))"""

        pg.init()
        screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        GAME_FONT = freetype.SysFont('Consolas', 12, bold=True)
        running =  True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            screen.fill((0,0,0))
            y = 100
            for i in modified_matrix:
                text_surface, rect = GAME_FONT.render(" "*0+i, (255, 255, 255)) #TODO : ajouter des couleurs et transparence !!!!
                screen.blit(text_surface, (100, y))
                y+=5

            pg.display.flip()

        pg.quit()
        


filename='test2.png'
image = Image.open(f'img/{filename}')
image = image.convert('1')

Ascii2D.display_image(Ascii2D,image)

