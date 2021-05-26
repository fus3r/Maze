import numpy as np

class Constants:
    import pygame.freetype as freetype
    freetype.init()
    
    WIDTH = 1920
    HEIGHT = 1080
    LARGEUR_DIF = 15 #Check issue
    GRADIENTS = ['.', '-', '/', 'r', 'L', 'o', '*', "'", '_', '|', 'c', 'C', 'a', '&', '`', '+', '(', 'v', 'J', 'h', '%', ',', '<', ')', 'u', 'U', 'k', '$', '^', 'i', '1', 'n', 'Y', 'b', '#', ':', '?', ']', 'x', 'X', 'd', '@']
    GAME_FONT = freetype.SysFont('Consolas', 12, bold=True)


class Images:
    def dimensions(self,filename:str,extension:str):
        from PIL import Image
        img = Image.open(f'img/{filename}.{extension}')
        return img.size

class Files:
    def path_join(lst:list):
        import os
        return os.path.join('',*lst)


    def clear_folder(path):
        import shutil,os
        """
        import os, glob
        files = glob.glob(f'{path}*')
        for f in files:
            os.remove(f)
        """
        shutil.rmtree(path)
        os.mkdir(path)



a=np.array
sq=lambda x:np.dot(x, x)
orth=lambda s:a([-s[1], s[0]])
norm=lambda x:((x[0])**2+(x[1])**2)**.5
angle_between = lambda a, b : np.arccos(np.dot(a, b)/(norm(a)*norm(b)))#à mettre dans utils
