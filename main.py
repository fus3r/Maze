from PIL import Image, ImageFont, ImageDraw, ImageColor, ImageFilter #Used for !owner get-info and will be used for DMS on member_join
import numpy as np

GRADIENTS = ['.', '-', '/', 'r', 'L', 'o', '*', "'", '_', '|', 'c', 'C', 'a', '&', '`', '+', '(', 'v', 'J', 'h', '%', ',', '<', ')', 'u', 'U', 'k', '$', '^', 'i', '1', 'n', 'Y', 'b', '#', ':', '?', ']', 'x', 'X', 'd', '@']

def rvb(color):
    try:
        a = GRADIENTS[(color*len(GRADIENTS)//255)]
    except:
        a = GRADIENTS[-1]
    return a



def main(longueur,largeur):
    image = Image.open('img/test2.png')
    image = image.convert('1')
    image.save('img/test2_black.jpg')
    image = Image.open('img/test2_black.jpg')
    
    long,larg = image.size
    
    long,larg=list(np.linspace(0, long, longueur,dtype=int)),list(np.linspace(0, larg, largeur,dtype=int))

    
    modified = [[0]*longueur for _ in range(largeur)]
    #print(modified)


    del long[-1]
    del larg[-1]
    
    for i,L in zip(range(longueur),long):
        for j,l in zip(range(largeur),larg):
            #print(L,l)
            color = image.getpixel((int(L),int(l)))
            print(f'{i} = {len(modified)}; {j} = {len(modified[i])} = {len(modified[0])}')
            modified[j][i] = rvb(color)
            
        

    for i in modified:
        o = ""
        for j in i:
            o+=str(j)
        
        print(o)
    
    return None



main(100,100)