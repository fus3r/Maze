from PIL import Image, ImageFont, ImageDraw, ImageColor, ImageFilter
import numpy as np

GRADIENTS = ['.', '-', '/', 'r', 'L', 'o', '*', "'", '_', '|', 'c', 'C', 'a', '&', '`', '+', '(', 'v', 'J', 'h', '%', ',', '<', ')', 'u', 'U', 'k', '$', '^', 'i', '1', 'n', 'Y', 'b', '#', ':', '?', ']', 'x', 'X', 'd', '@']

def rvb(color):
    try:
        symbol = GRADIENTS[(color*len(GRADIENTS)//255)]
    except:
        symbol = GRADIENTS[-1]
    return symbol



def main(longueur,largeur,filename,ext):
    image = Image.open(f'img/{filename}.{ext}')
    image = image.convert('1')
    image.save(f'img/{filename}_black.{ext}')
    image = Image.open(f'img/{filename}_black.{ext}')
    
    long,larg = image.size
    
    
    long,larg=list(np.linspace(0, long, longueur,dtype=int)),list(np.linspace(0, larg, largeur,dtype=int))

    print(long,larg)
    modified = [[0]*longueur for _ in range(largeur)]
    #print(modified)


    del long[-1]
    del larg[-1]
    
    for indexModified_longueur,indexColor_longueur in zip(range(longueur),long):
        for indexModified_largeur,indexColor_largeur in zip(range(largeur),larg):
            #print(L,l)
            #print(int(indexColor_longueur),int(indexColor_largeur))
            color = image.getpixel((int(indexColor_longueur),int(indexColor_largeur)))
            #print(f'{i} = {len(modified)}; {j} = {len(modified[i])} = {len(modified[0])}')
            modified[indexModified_largeur][indexModified_longueur] = rvb(color)
            
        

    for i in modified:
        print("".join([str(k) for k in i]))
    
    return None



main(200,100,'zemmour','jpg')