import numpy as np 
import matplotlib.pyplot as plt 
from coeffs import *
P=np.array([1,-1])
n=np.array([2,1])
c=3
m=np.array([1,-1])
d=1
i=(n,m)
e=np.array([c,d])
O=np.linalg.inv(i)@e
print(O)
f=dir_vec(O,P)
print(f)
g=f@P
print(g)
r=np.sqrt((P[0]-O[0])**2+(P[1]-O[1])**2)
print(r)
m1=omat@f
A1=y_icept(f,g)
k1=-1
k2=1
x_line=line_dir_pt(m1,A1,k1,k2)
len=100

theta=np.linspace(0,2*np.pi,len)
x_circ =np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T+O).T
x_OP=line_gen(O,P)
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')
plt.plot(x_OP[0,:],x_OP[1,:],label= "$OP$")
plt.plot(O[0],O[1],'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1+0.1),P[1]*(1-0.1),'P')
plt.plot(x_line[0,:],x_line[1,:],label='$tangent$')
plt.title('circle7')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid()#minor
plt.axis('equal')
plt.show()

