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

        try:
            symbol = self.GRADIENTS[(color*len(self.GRADIENTS)//255)]
        except:
            symbol = self.GRADIENTS[-1]
        return symbol


    def pic_to_matrix(self,longueur:int,largeur:int,filename:str,ext:str):
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

    """
    def pic_to_matrix2(self,longueur:int,largeur:int,filename:str,ext:str):
        image = Image.open(f'img/{filename}.{ext}')
        image = image.convert('1')
        image.save(f'img/{filename}_black.{ext}')
        image = Image.open(f'img/{filename}_black.{ext}')
        


        long,larg = image.size
        print(long,larg)

        image = image.resize((longueur,largeur), Image.ANTIALIAS)
        image.save(f'img/{filename}_black.{ext}')

        image = Image.open(f'img/{filename}_black.{ext}')
        long,larg = image.size
        
        print(long,larg)
        


        I = np.asarray(image)
        matrix = Image.fromarray(np.uint8(I))
        
        pixels = list(image.getdata())


        return pixels
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
        
        
matrix = Ascii2D.pic_to_matrix(Ascii2D,210,100,'zemmour','jpg')
modified_matrix = Ascii2D.transform(Ascii2D,matrix)
Ascii2D.display(Ascii2D,modified_matrix)


