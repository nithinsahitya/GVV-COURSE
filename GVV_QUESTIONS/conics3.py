import numpy as np
import matplotlib.pyplot as plt

#Given information
O=np.array([0,0])
e=3/5
g=6
a=6/2
a=a*5/3
print(a)
b=a*np.sqrt(1-e**2)
print(b)

#foci of ellipse
F1=np.array([a*e,0])
F2=np.array([-a*e,0])

#Vertices of quadrilateral
A=np.array([a,0])
B=np.array([-a,0])
C=np.array([0,b])
print(C)
D=np.array([0,-b])

#Area of ellipse
Area=2*a*b
print("The area of quadrilateral inscribed in ellipse is",Area)
len=100
theta=np.linspace(0,2*np.pi,len)
y=np.zeros((2,len))
y[0,:]=a*np.cos(theta)
y[1,:]=b*np.sin(theta)
plt.plot(y[0,:],y[1,:],label='Ellipse')
plt.plot([A[0],D[0]],[A[1],D[1]])
plt.plot([A[0],C[0]],[A[1],C[1]])
plt.plot([B[0],C[0]],[B[1],C[1]])
plt.plot([B[0],D[0]],[B[1],D[1]])
plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1-0.2),A[1]*(1+0.8),'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(0.9),B[1]*(1-0.1),'B')
plt.plot(C[0],C[1],'o')
plt.text(C[0]*(1),C[1]*(0.8),'C')
plt.plot(D[0],D[1],'o')
plt.text(D[0]*(1+0.02),D[1]*(1-0.1),'D')
plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1-0.1),O[1]*(1+0.1),'O')
plt.title('conics3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.grid()
plt.axis('equal')
plt.show()