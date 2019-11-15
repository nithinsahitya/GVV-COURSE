import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
A=np.array([2,3])
B=np.array([4,5])
n=np.array([-1,4])
c=3
C=(A+B)/2
print(C)
m=dir_vec(A,B)
print(m)
e=np.array([1,1])
c1=7
i=(n,e)
d=np.array([c,c1])
O=np.linalg.inv(i)@d
print(O)
r=np.linalg.norm(O-A)
print(r)
m1=omat@n
A1=y_icept(n,c)
k1=-1.5
k2=1.5
x_line=line_dir_pt(m1,A1,k1,k2)
len=100

theta=np.linspace(0,2*np.pi,len)
x_circ =np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T+O).T
x_AB=line_gen(A,B)
x_OC=line_gen(O,C)
plt.plot(x_AB[0,:],x_AB[1,:],label= "$AB$")
plt.plot(x_OC[0,:],x_OC[1,:],label= "$OC$")
plt.plot(x_line[0,:],x_line[1,:],label='$given equation$')
plt.plot(A[0],A[1], 'o')
plt.text(A[0]*(1-0.1),A[1]*(1+0.1),'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1-0.2),B[1]*(1),'B')
plt.plot(C[0],C[1], 'o')
plt.text(C[0]*(1-0.1),C[1]*(1+0.1),'C')
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')
plt.plot(O[0],O[1],'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')
plt.title('circle1')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid()#minor
plt.axis('equal')
plt.show()

