import numpy as np
import matplotlib.pyplot as plt
import math as m
from coeffs import *



def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


e1=np.array([1,0])
e2=np.array([0,1])
P=np.array([2,1])
n=np.array([1,-1])
c = 4
d=2*np.sqrt(3)
omat=np.array([[0,1],[-1,0]])
m = omat@n
lam=d/np.linalg.norm(m)
Q=P+lam*m
A=np.array([c/(n@e1),0])
B=np.array([0,c/(n@e2)])
Aug=(n,m)
c1=m@Q
cs=np.array([c,c1])
C=np.linalg.inv(Aug)@cs
print(C)



x_AB= line_gen(A,B)
x_CQ= line_gen(C,Q)


#Plot the line AB
plt.plot(x_AB[0,:],x_AB[1,:],label='$L$')
plt.plot(x_CQ[0,:],x_CQ[1,:],label='$CQ$')



plt.grid() # minor
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 - 0.1), C[1] * (1 + 0.1) , 'C')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 - 0.2), Q[1] * (1) , 'Q')
plt.xlabel('$x$')
plt.ylabel('$y$')

plt.show()
