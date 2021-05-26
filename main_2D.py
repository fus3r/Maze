from utils import *
from PIL import Image
import numpy as np
import pygame as pg

class Ascii2D:

    GRADIENTS = Constants.GRADIENTS
    HEIGHT = Constants.HEIGHT
    WIDTH = Constants.WIDTH
    LARGEUR_DIF = Constants.LARGEUR_DIF
    GAME_FONT = Constants.GAME_FONT

    def rvb(self,color:int, mode=0):
        """Returns symbol using color code given by image.getpixel

        Args:
            color (int): color code

        Returns:
            symbol (str): Symbol
        """
        ind=color*(len(self.GRADIENTS)-1)/255
        assert ind<len(self.GRADIENTS), "GORGE"
        if mode==1:
            assert color!=1 or color!=0, f"color = {color}"
            ind=color*(len(self.GRADIENTS)-1)
            assert ind==int(ind), "RVB mode problem"
        assert ind<=len(self.GRADIENTS)-1, "trhythdrtjx"
        symbol = self.GRADIENTS[int(ind)]
        return symbol

    def pic_to_matrix(self,longueur:int,filename:str,ext:str):
        image = Image.open(f'img/{filename}.{ext}')
        image = image.convert('1')
        image.save(f'img/{filename}_black.{ext}')
        image = Image.open(f'img/{filename}_black.{ext}')
        
        long,larg = image.size
        largeur = int(longueur*larg/long)-self.LARGEUR_DIF

        long,larg=list(np.linspace(0, long-1, longueur,dtype=int)),list(np.linspace(0, larg-1, largeur,dtype=int))

        return [[image.getpixel((int(indexColor_longueur),int(indexColor_largeur))) for indexColor_longueur in long] for indexColor_largeur in larg]

    def pic_to_matrix2(self,longueur:int,largeur:int,filename:str,ext:str):
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
        running =  True

        while running:
            """
            screen.fill((0,0,0))
            y = 100
            for i in modified_matrix:
                text_surface, rect = self.GAME_FONT.render(i, (255, 255, 255)) #TODO : ajouter des couleurs et transparence !!!!
                screen.blit(text_surface, (100, y))
                y+=5
            """
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            
            screen.fill((0,0,0))
            y = 100
            for i in modified_matrix:
                text_surface,_ = self.GAME_FONT.render("".join([str(k) for k in i]), (255, 255, 255))
                screen.blit(text_surface, (200, y))
                y+=12

            pg.display.flip()
        pg.quit()
        

        

        
        

'''
dimensions = Images.dimensions(Images,'zemmour','jpg')
matrix = Ascii2D.pic_to_matrix(Ascii2D,210,'zemmour','jpg')
modified_matrix = Ascii2D.transform(Ascii2D,matrix)
Ascii2D.display(Ascii2D,modified_matrix)
'''

if __name__=='__main__':
    matrix = Ascii2D.pic_to_matrix(Ascii2D,210,'test2','png')
    modified_matrix = Ascii2D.transform(Ascii2D,matrix)
    Ascii2D.display(Ascii2D,modified_matrix)

