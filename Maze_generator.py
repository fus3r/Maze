from hashlib import new
from main_2D import Ascii2D
import random as r         
from utils import *


class MazeGen:

    def in_maze(self,full,neighbors):
        for i in neighbors:
            if i[0]<0 or i[1]<0:
                neighbors.remove(i)
        
        for i in neighbors:
            try:
                full[i[0]][i[1]]
            except:
                neighbors.remove(i)
        return neighbors

    def generate_maze(self,x,y):
        lab=[[r.choice([" ","#"]) for _ in range(x)] for _ in range(y)]
        return lab

    def full_maze(self,x,y):
        return [["#" for _ in range(x)] for _ in range(y)]

    def maze(self,full,start_point:tuple,previous_neighbors:list):
        x0,y0=start_point[0],start_point[1]
        if x0==len(full[0])-1 and y0==len(full)-1:
            return full
        
        full[x0][y0] = " "
        neighbors = MazeUtils.neighbors(x0,y0,diagonals=False)
        neighbors = self.in_maze(self,full,neighbors)
        
        new_start_point = r.choice(neighbors)
        print(f'Current neighbors : {neighbors}\nPrevious neighbors : {previous_neighbors}')
        if previous_neighbors is not None:
            while new_start_point in previous_neighbors: #and MazeUtils.neighbors(new_start_point[0],new_start_point[1],diagonals=False).count(" ")>=2:
                new_start_point = r.choice(neighbors)
            neighbors+=previous_neighbors
        print(f'Choice made : {new_start_point}')
        #print(new_start_point,MazeUtils.neighbors(new_start_point[0],new_start_point[1],diagonals=False).count(" "))
        """
        neighbors = MazeUtils.neighbors(x0,y0,diagonals=True)
        neighbors = self.in_maze(self,full,neighbors)
        """
        neighbors.append((x0,y0))
        
        for i in full:  print(*i)
        print("\n")
        
        return self.maze(self,full,new_start_point,neighbors)




if __name__=='__main__':
    """
    for x in MazeGen.generate_maze(MazeGen,10,10):
        print(*x)
    """
    print("\n")
    for i in MazeGen.maze(MazeGen,MazeGen.full_maze(MazeGen,20,20),(0,0),None):
        print(*i)
    
