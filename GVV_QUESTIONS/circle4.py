import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
e=np.array([-2,0])
O1=-e/2
print(O1)
r1=O1.T@O1
print(r1)
n=np.array([1,1])
c=3
m=omat@n
print(m)
c1=m@O1
print(c1)
i=(n,m)
d=np.array([c,c1])
C=np.linalg.inv(i)@d
print(C)
O2=2*C-O1
print(O2)
m1=omat@n
A_1=y_icept(n,c)
k1=0
k2=4
len=100
theta=np.linspace(0,2*np.pi,len)
x_circ=np.zeros((2,len))
x_circ[0,:] = r1*np.cos(theta)
x_circ[1,:] = r1*np.sin(theta)
x_circ = (x_circ.T+O1).T

plt.plot(x_circ[0,:],x_circ[1,:],label='$circle1$')
plt.plot(O1[0],O1[1],'o')
plt.text(O1[0] * (1 + 0.1), O1[1] * (1 - 0.1) , 'O1')
len=100
theta=np.linspace(0,2*np.pi,len)
x_circ=np.zeros((2,len))
x_circ[0,:] = r1*np.cos(theta)
x_circ[1,:] = r1*np.sin(theta)
x_circ = (x_circ.T+O2).T

x_line=line_dir_pt(m1,A_1,k1,k2)
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle2$')
plt.plot(O2[0],O2[1],'o')
plt.text(O2[0] * (1 + 0.1), O2[1] * (1 - 0.1) , 'O2')
plt.plot(x_line[0,:],x_line[1,:],label='$given equation$')
plt.title('circle4')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid()
plt.axis('equal')
plt.show()

