from PIL import Image
import numpy as np

class Ascii2D:


    GRADIENTS = ['.', '-', '/', 'r', 'L', 'o', '*', "'", '_', '|', 'c', 'C', 'a', '&', '`', '+', '(', 'v', 'J', 'h', '%', ',', '<', ')', 'u', 'U', 'k', '$', '^', 'i', '1', 'n', 'Y', 'b', '#', ':', '?', ']', 'x', 'X', 'd', '@']

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



    def transform(self,longueur:int,largeur:int,filename:str,ext:str):
        """Transform image (any extension) to ASCII Art

        Args:
            longueur (int): Length desired
            largeur (int): Width desired
            filename (str): Filename
            ext (str): Filename extension

        Returns:
            None:
        """

        image = Image.open(f'img/{filename}.{ext}')
        image = image.convert('1')
        image.save(f'img/{filename}_black.{ext}')
        image = Image.open(f'img/{filename}_black.{ext}')
        
        long,larg = image.size

        assert (longueur<long and largeur<larg), "Invalid width or length"
        
        long,larg=list(np.linspace(0, long, longueur,dtype=int)),list(np.linspace(0, larg, largeur,dtype=int))

        modified = [[0]*longueur for _ in range(largeur)]
    

        del long[-1]
        del larg[-1]
        
        for indexModified_longueur,indexColor_longueur in zip(range(longueur),long):
            for indexModified_largeur,indexColor_largeur in zip(range(largeur),larg):
                color = image.getpixel((int(indexColor_longueur),int(indexColor_largeur)))
                modified[indexModified_largeur][indexModified_longueur] = self.rvb(color)
                
            

        for i in modified:
            print("".join([str(k) for k in i]))
        
        return None



Ascii2D.transform(210,100,'test2','png')