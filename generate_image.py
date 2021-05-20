from scipy.spatial.transform import Rotation as R
from utils import *
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def drawline(mat, a, b):
    """
    dessine une ligne entre les points a, b sur l'image mat
    ne return rien
    """
    step=.5
    dist=((a[0]-b[0])**2+(a[1]-b[1])**2)**.5
    x=(a[0], a[1])
    dir=((b[0]-a[0])*step/dist, (b[1]-a[1])*step/dist)
    while dist>step:
        dist = ((a[0]-b[0])**2+(a[1]-b[1])**2)**.5  
        x=(x[0]+dir[0], x[1]+dir[1])
        o, p = x[0], x[1]
        o, p = int(o), int(p)
        if o<0 or p<0 or o>=len(mat) or p >=len(mat[0]):
            break
        mat[o][p] = 255   



def generate_image(anglex, angley, w, h):
    """
    w, h : la longueur et la hauteur de l'output (res)
    anglex, angley : les angles de rotation du cube
    res (output) : int[][] dans [|0, 255|]
    Génère et return une matrice (int[][]) (image) d'un cube ayant subi une rotation de angle(rad), valeurs dans [0;255]
    """

    res=[[0 for i in range(w)] for j in range(h)] #le resultat à return #TODO : le faire avec np
    points=[] #On crée la liste de (tuples représentant les coordonnées des points d'un cube)
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if (i, j, k) == (0, 0, 0):
                    continue
                points.append((i, j, k+10))
    #matrice de rotation 
    #https://fr.wikipedia.org/wiki/Matrice_de_rotation
    r = R.from_quat([0, 0, np.sin(anglex), np.cos(angley)])
    r = r.as_matrix()

    #on fait rotater les points (ce mot existe)
    #https://fr.wiktionary.org/wiki/rotater
    points = [tuple(np.matmul(p, r)) for p in points]

    #On projette ces points sur le plan xy (en prenant que les 2 premières coordonnées)
    #relier tous les points entre eux sur l'image resultat (res)
    for i in points:
        for j in points:
            drawline(res, i, j)
    return res

img = generate_image(.4, 5.5, 100, 100)
#img = Image.fromarray(np.asarray(img))
plt.show()

from main_2D import Ascii2D


i=0
while True:
    i+=1
    img=generate_image(.4+i*.025, 5.5+i*.01, 200, 200)
    array = np.array(img, dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image.save(f'img/generate_img/new{i}.png')
    matrix = Ascii2D.pic_to_matrix(Ascii2D,200,f'generate_img/new{i}','png')
    modified_matrix = Ascii2D.transform(Ascii2D,matrix)
    Ascii2D.display(Ascii2D,modified_matrix)

    '''
    plt.imshow(img)
    plt.imshow(img, cmap='gray')
    plt.pause(.01)
    '''
    if i >=20:
        break

Files.clear_folder(Files.path_join(['img','generate_img']))
    
    