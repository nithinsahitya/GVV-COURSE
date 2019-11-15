import numpy as np
import matplotlib.pyplot as plt

a1=4
b1=1
a2=16
b2=np.sqrt(16/15)
A=np.array([4,1])
B=np.array([4,-1])
C=np.array([-4,-1])
D=np.array([-4,1])
O=np.array([0,0])
len=100
theta=np.linspace(0,2*np.pi,len)
x1=a1*np.cos(theta)
y1=b1*np.sin(theta)
x2=a2*np.cos(theta)
y2=b2*np.sin(theta)
plt.plot(x1,y1,'b')
plt.plot(x2,y2,'y')
plt.plot([A[0],B[0]],[A[1],B[1]],'b')
plt.plot([B[0],C[0]],[B[1],C[1]],'b')
plt.plot([C[0],D[0]],[C[1],D[1]],'b')
plt.plot([D[0],A[0]],[D[1],A[1]],'b')
plt.plot([A[0],B[0]],[A[1],B[1]],'o')
plt.plot([B[0],C[0]],[B[1],C[1]],'o')
plt.plot([C[0],D[0]],[C[1],D[1]],'o')
plt.plot([D[0],A[0]],[D[1],A[1]],'o')
plt.plot(O[0],O[1],"o")
plt.text(O[0]*(1+0.1),O[1]*(1-0.1),"O")
plt.grid()
plt.axis("equal")
plt.show()