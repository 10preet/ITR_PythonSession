import numpy as np

A=np.array([[1,2,3],
            [2,3,4]])
B=np.array([[1,2],
            [3,4],
            [4,5]])
C=A@B
print(C)