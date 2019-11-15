import numpy as np
import matplotlib.pyplot as plt

#Given parameters of hyperbola
a=9
b=-18
c=5
e=-b+np.sqrt(b**2-4*a*c)
e=e/(2*a)
print(e)
S=np.array([5,0])
c=9

V=np.array([[16,0],[0,-9]])

print(V)
c1=144
a1=c1/V[0][0]
b1=c1/V[1][1]
print(a1,b1)

#Difference of a^2-b^2
D=a1**2-b1**2
print(D)


plt.plot(S[0],S[1],'o')
plt.text(S[0]*(1-0.1),S[1]*(1-0.1),'S')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="upper right")
plt.grid()
plt.axis('equal')
plt.show()