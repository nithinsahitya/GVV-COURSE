import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

P=np.array([-2,4])
Q=np.array([0,2])
m=np.array([0,1])
c=m@Q
i=np.array([[1,-1],[0,1]])
n=-4
c1=np.array([n,c])

O=np.linalg.inv(i)@c1
r=np.linalg.norm(O-P)
print(O,r)
n_1=np.array([4,5])
c_1=6

n_2=np.array([2,-3])
c_2=-10

n_3=np.array([3,4])
c_3=3

n_4=np.array([5,2])
c_4=-4

if n_1@O == c_1:
    print('(i) is a diameter')
else:
    print('(i) is not a diameter')
    
if n_2@O == c_2:
    print('(ii) is a diameter')
else:
    print('(ii) is not a diameter')
    
if n_3@O == c_3:
    print('(iii) is a diameter')
else:
    print('(iii) is not a diaemeter')
    
if n_4@O == c_4:
    print('(iv) is a diameter')
else:
    print('(iv) is not a diameter')

m_1=omat@n_1
A_1=y_icept(n_1,c_1)
m_2=omat@n_2
A_2=y_icept(n_2,c_2)
m_3=omat@n_3
A_3=y_icept(n_3,c_3)
m_4=omat@n_4
A_4=y_icept(n_4,c_4)

k1=-1
k2=1

x_1=line_dir_pt(m_1,A_1,k1,k2)
x_2=line_dir_pt(m_2,A_2,k1,k2)
x_3=line_dir_pt(m_3,A_3,k1,k2)
x_4=line_dir_pt(m_4,A_4,k1,k2)
    
    
len=100

theta=np.linspace(0,2*np.pi,len)
x_circ =np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T+O).T
x_PQ=line_gen(P,Q)
x_OQ=line_gen(O,Q)
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_OQ[0,:],x_OQ[1,:],label='$r$')
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')
plt.plot(O[0],O[1],'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')
plt.plot(P[0],P[1], 'o')
plt.text(P[0]+0.01,P[1]+0.02,'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1-0.2),Q[1]*(1),'Q')
plt.plot(x_1[0,:],x_1[1,:],label='$i$')
plt.plot(x_2[0,:],x_2[1,:],label='$ii$')
plt.plot(x_3[0,:],x_3[1,:],label='$iii$')
plt.plot(x_4[0,:],x_4[1,:],label='$iv$')
plt.title('circle6')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid()#minor
plt.axis('equal')
plt.show()
