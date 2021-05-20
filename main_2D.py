from utils import *
from PIL import Image
import numpy as np
import pygame as pg
import pygame.freetype as freetype

class Ascii2D:

    GRADIENTS = Constants.GRADIENTS
    HEIGHT = Constants.HEIGHT
    WIDTH = Constants.WIDTH

    def rvb(self,color:int):
        """Returns symbol using color code given by image.getpixel

        Args:
            color (int): color code

        Returns:
            symbol (str): Symbol
        """
        ind=color*(len(self.GRADIENTS)-1)/255
        assert ind<len(self.GRADIENTS), "GORGE"
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


    def transform(self,matrix:list):
        """Transform image (any extension) to ASCII Art

        Args:
            longueur (int): Length desired
            largeur (int): Width desired
            filename (str): Filename
            ext (str): Filename extension

        Returns:
            None:
        """

        w, h = len(matrix), len(matrix[0])
        res=['' for j in range(w)] #TODO creer avec np
        #assert (longueur<long and largeur<larg), "Invalid width or length"
        longueur = len(matrix)
        largeur = len(matrix[0])

        #modified = [[0]*longueur for _ in range(largeur)]
    
        
        for i in range(longueur):
            for j in range(largeur):
                res[i] += self.rvb(self, matrix[i][j])
                
        
        
        return res

    def display(self,modified_matrix):
        for i in modified_matrix:
            print("".join([str(k) for k in i]))

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
                text_surface, rect = GAME_FONT.render("".join([str(k) for k in i]), (255, 255, 255))
                screen.blit(text_surface, (0, y))
                y+=10

            pg.display.flip()

        pg.quit()
        
        
matrix = Ascii2D.pic_to_matrix(Ascii2D,480//2,200//2,'zemmour','jpg')
modified_matrix = Ascii2D.transform(Ascii2D,matrix)
Ascii2D.display(Ascii2D,modified_matrix)


