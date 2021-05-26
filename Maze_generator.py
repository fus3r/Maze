from main_2D import Ascii2D

import random as r                  

def generer_lab(x,y):
    lab=[[r.choice([" ","|"]) for _ in range(x)] for _ in range(y)]
    return lab
for x in generer_lab(10,10):
    print(*x)
