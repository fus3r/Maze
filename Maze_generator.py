from hashlib import new
from main_2D import Ascii2D
import random as r         
from utils import *


class MazeGen:

    def in_maze(self,full,neighbors):
        for i in neighbors:
            try:
                full[i]
            except:
                del i
        return neighbors

    def generate_maze(self,x,y):
        lab=[[r.choice([" ","#"]) for _ in range(x)] for _ in range(y)]
        return lab

    def full_maze(self,x,y):
        return [["#" for _ in range(x)] for _ in range(y)]

    def maze(self,full,start_point:tuple,previous_neighbors:list):
        x0,y0=start_point[0],start_point[1]
        if x0>=len(full[0])-1 or y0>=len(full)-1:
            return full
        full[x0][y0] = " "
        neighbors = MazeUtils.neighbors(x0,y0,diagonals=False)
        neighbors = self.in_maze(self,full,neighbors)
        new_start_point = r.choice(neighbors)
        neighbors.append((x0,y0))
        if previous_neighbors is not None:
            while new_start_point in previous_neighbors:
                new_start_point = r.choice(neighbors)
        for i in full:  print(*i)
        print("\n")
        return self.maze(self,full,new_start_point,neighbors)




if __name__=='__main__':
    """
    for x in MazeGen.generate_maze(MazeGen,10,10):
        print(*x)
    """
    print("\n")
    for i in MazeGen.maze(MazeGen,MazeGen.full_maze(MazeGen,20,20),(10,10),None):
        print(*i)
    
