import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
P=np.array([4,7])
O=np.array([0,0])
c=9
r=np.sqrt(9)
a=1
b=2*P
print(b)
c=round(np.linalg.norm(P))**2-9
print(c)
print("The Product of roots PA and PB:",c)
len=100
theta=np.linspace(0,2*np.pi,len)
x_circ=np.zeros((2,len))
x_circ[0,:]=r*np.cos(theta)
x_circ[1,:]=r*np.sin(theta)
x_circ=(x_circ.T+O).T
A=np.array([x_circ[0,:][62],x_circ[1,:][62]])
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')
plt.plot([P[0],x_circ[0,:][62]],[P[1],x_circ[1,:][62]])
plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1+0.1),O[1]*(1-0.1),'O')
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1),P[1]*(0.9),'P')
plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1+0.1),A[1]*(1-0.1),'A')
plt.title('circle3')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid()
plt.axis('equal')
plt.show()

