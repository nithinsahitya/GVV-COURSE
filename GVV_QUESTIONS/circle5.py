import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
m=np.array([2*-2,2*3])
c1=12
O1=-m/2
print(O1)
O2=np.array([-3,2])
print(O2)
r1=np.sqrt(O1.T@O1+c1)
print(r1)
e=np.linalg.norm(O1-O2)
print(e)
r2=np.sqrt(e**2+r1**2)
print(r2)
len=100

theta=np.linspace(0,2*np.pi,len)
x_circ =np.zeros((2,len))
x_circ[0,:] = r1*np.cos(theta)
x_circ[1,:] = r1*np.sin(theta)
x_circ = (x_circ.T+O1).T

plt.plot(x_circ[0,:],x_circ[1,:],label='$circle1$')
plt.plot(O1[0],O1[1],'o')
plt.text(O1[0] * (1 + 0.1), O1[1] * (1 - 0.1) , 'O1')
len=100

theta=np.linspace(0,2*np.pi,len)
x_circ =np.zeros((2,len))
x_circ[0,:] = r2*np.cos(theta)
x_circ[1,:] = r2*np.sin(theta)
x_circ = (x_circ.T+O2).T
x_O1O2=line_gen(O1,O2)
plt.plot(x_O1O2[0,:],x_O1O2[1,:],label='$O1O2$')
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle2$')
plt.plot(O2[0],O2[1],'o')
plt.text(O2[0] * (1 + 0.1), O2[1] * (1 - 0.1) , 'O2')


plt.title('circle5')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid()#minor
plt.axis('equal')
plt.show()
