import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
P=np.array([2,2])
n=np.array([2,-4])
c=-4
r1=3
O2=-n/2
print(O2)
r2=np.sqrt(4+(O2.T@O2))
print(r2)
O1=2*P-O2
print(O1)
m=np.array([1,0])
A=(np.linalg.norm(m))**2
B=-2*m.T@O1
C=(np.linalg.norm(O1))**2-(r1)**2
lam1=-B+np.sqrt(B**2-4*A*C)
lam1=lam1/2*A
print(lam1)
lam2=-B-np.sqrt(B**2-4*A*C)
lam2=lam2/2*A
print(lam2)

len=100

theta=np.linspace(0,2*np.pi,len)
x_circ =np.zeros((2,len))
x_circ[0,:] = r1*np.cos(theta)
x_circ[1,:] = r1*np.sin(theta)
x_circ = (x_circ.T+O1).T

plt.plot(x_circ[0,:],x_circ[1,:],label='$circle1$')
plt.plot(O1[0],O1[1],'o')
plt.text(O1[0] * (0.9), O1[1] * (0.8) , 'O1')
len=100

theta=np.linspace(0,2*np.pi,len)
x_circ =np.zeros((2,len))
x_circ[0,:] = r2*np.cos(theta)
x_circ[1,:] = r2*np.sin(theta)
x_circ = (x_circ.T+O2).T
x_O1P=line_gen(O1,P)
x_O2P=line_gen(O2,P)
plt.plot(x_O1P[0,:],x_O1P[1,:],label='$r1$')
plt.plot(x_O2P[0,:],x_O2P[1,:],label='$r2$')
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle2$')
plt.plot(O2[0],O2[1],'o')
plt.text(O2[0] * (0.9), O2[1] * (0.8) , 'O2')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1), P[1] * (1) , 'P')
plt.title('circle2')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid()#minor
plt.axis('equal')
plt.show()


