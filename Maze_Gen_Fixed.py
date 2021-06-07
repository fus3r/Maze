import random as r

x = 20
y = 20

def in_maze(full,neighbors):
    for i in neighbors:
        try:
            full[i]
        except:
            del i
    return neighbors

def full_maze(x,y):
        return [["#" for _ in range(x)] for _ in range(y)]


def maze(full,x0,y0,x_fin,y_fin):
    full[x0][y0] = " "
    if x0 == x_fin or y0 == y_fin:
        return full
    neighbors = [(i,j) for i in [x0-1,x0,x0+1] for j in [y0-1,y0,y0+1] if i >= 0 and j >= 0 and i<x and j<y and i != x0 and j!= y0]
    neighbors = in_maze(full,neighbors)
    return maze(full,r.choice(neighbors)[0],r.choice(neighbors)[1],x_fin,y_fin)

for i in maze(maze(full_maze(x,y),0,0,x-1,y-1),x-1,y-1,0,0):
    print(*i)
    
