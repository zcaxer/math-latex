import  numpy as np
from sympy import Matrix

x= np.matrix([[1,1,1],[1,2,3],[1,3,5]])
y= np.matrix([[1,-1,1],[0,1,-2],[0,0,1]])
m=Matrix(x)
m1=Matrix(y)
m2=m1.transpose()

print(m2*m*m1)

