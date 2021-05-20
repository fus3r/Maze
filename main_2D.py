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

    def rvb(self,color:int):
        """Returns symbol using color code given by image.getpixel

        Args:
            color (int): color code

        Returns:
            symbol (str): Symbol
        """

        try:
            symbol = self.GRADIENTS[int(color*len(self.GRADIENTS)/255)]
        except:
            symbol = self.GRADIENTS[-1]
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

    """
    def pic_to_matrix2(self,longueur:int,largeur:int,filename:str,ext:str):
        image = Image.open(f'img/{filename}.{ext}')
        image = image.convert('1')
        image.save(f'img/{filename}_black.{ext}')
        image = Image.open(f'img/{filename}_black.{ext}')

        return np.asarray(image.resize((longueur, largeur), resample=2))
    """

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

        #assert (longueur<long and largeur<larg), "Invalid width or length"
        longueur = len(matrix[0])
        largeur = len(matrix)

        #modified = [[0]*longueur for _ in range(largeur)]
    
        
        for indexModified_longueur in range(longueur):
            for indexModified_largeur in range(largeur):
                matrix[indexModified_largeur][indexModified_longueur] = self.rvb(self,matrix[indexModified_largeur][indexModified_longueur])
                
        
        
        return matrix

    def display(self,modified_matrix):
        for i in modified_matrix:
            print("".join([str(k) for k in i]))

        pg.init()
        screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        running =  True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            screen.fill((0,0,0))
            y = 100
            for i in modified_matrix:
                text_surface, rect = self.GAME_FONT.render("".join([str(k) for k in i]), (255, 255, 255))
                screen.blit(text_surface, (200, y))
                y+=12

            pg.display.flip()

        pg.quit()
        

dimensions = Images.dimensions(Images,'zemmour','jpg')
matrix = Ascii2D.pic_to_matrix(Ascii2D,210,'test2','png')
modified_matrix = Ascii2D.transform(Ascii2D,matrix)
Ascii2D.display(Ascii2D,modified_matrix)


