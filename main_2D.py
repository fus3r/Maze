from utils import *
from PIL import Image
import numpy as np
#import pygame as pg

class Ascii2D:

    GRADIENTS = Constants.GRADIENTS

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
                
            

        for i in matrix:
            print("".join([str(k) for k in i]))
        
        return None





matrice = Ascii2D.pic_to_matrix(Ascii2D,210,100,'zemmour','jpg')
Ascii2D.transform(Ascii2D,matrice)
