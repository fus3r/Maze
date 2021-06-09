import numpy as np


norm = lambda x : ((x[0])**2 +(x[1])**2)**.5
normalize = lambda x : x/norm(x)
orth = lambda x: np.array(-x[1], x[0])