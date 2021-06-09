
import numpy as np
from PIL import Image
from utils import *
import PIL
from vecmaths import *
import matplotlib.pyplot as plt





'''
https://www.youtube.com/watch?v=gYRrGTC7GtA
https://www.youtube.com/watch?v=PC1RaETIx3Y

'''
class Player:

    def __init__(self)-> None:
        self.pos=np.array([9, 7]) #Position 2D de Player
        self.dir=np.array([15, 6]) #Direction du regard
        self.cam_size=50, 100 #Dimensions de l'écran (h, w)(en pixels)
        self.screen_scale = 1
        self.screen_dist = .5
        return


    def generate_image(self, map):
        '''
            La map une matrice de zéros (vide) et de uns (murs)
        '''

        w=self.cam_size[1]
        for i in range(w):
            PE=dir*self.screen_dist+orth(dir)*(i-w//2)/self.screen_scale
            P= self.pos
            d=0
            v, w = PE

            pointer=P+0
            while True:
                

                if v!=0:
                    if up:
                        


        render_image=np.zeros(self.cam_size)
        self.dir = normalize(self.dir)


        return render_image

    def test(self):
        for _ in range(5):
            img=self.generate_image()
            img=Image.fromarray(img, mode='L')
            img=img.resize((800, 600), resample=Image.NEAREST)
            img.show()
            self.rotate(.1)


img=PIL.Image.open('img/Map.png')

pix = np.array(img.getdata()).reshape(img.size[0], img.size[1], 3)

print(pix)
out=  np.array([[0 for i in range(len(pix[0]))] for j in range(len(pix))])
k=None
for j in range(len(pix)):
    for i in range(len(pix[0])):
        c=pix[j][i][0] == pix[j][i][1]
        if not c:
            k=i, j
        
        a=(np.average(pix[j][i])<10)*c
        out[j][i] = a
        print("Av", a, out[j][i])

#print(list(k))
print(out)
out=np.array(out)
print(out)
player= Player()

plt.imshow(player.generate_image(out))
plt.show()