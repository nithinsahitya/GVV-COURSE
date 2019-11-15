import numpy as np
import matplotlib.pyplot as plt

def y_icept(n,c):
    A = np.zeros(2)
    m_y = np.array([0,1])
    A[0] = 0
    A[1] = c/(n@m_y)
    return A
def line_dir_pt(m,A,k1,k2):
    len =10
    x_AB = np.zeros((2,len))
    lam_1 = np.linspace(k1,k2,len)
    for i in range(len):
        temp1 = A + lam_1[i]*m
        x_AB[:,i]= temp1.T
    return x_AB
omat = np.array([[0,1],[-1,0]]) 

#Given parameters of ellipse
V=np.array(([25,0],[0,9]))
c=225
P=np.array([3/2,5*np.sqrt(3)/2])

V1=np.array([25/c,0/c])
V2=np.array([0/c,9/225])
V=(V1,V2)
print(V)
#By comparing ellipse equation with xTVx+uTx+F=0
u=0
F=-1
a=np.sqrt(-F/V1[0])
print(a)
b=np.sqrt(-F/V2[1])
print(b)

#Equation of desired tangent
e=(V@P).T
print(e)
c1=1
F1=np.array([0,a*np.sqrt((b**2-a**2)/a**2)])
F2=np.array([0,-a*np.sqrt((b**2-a**2)/a**2)])

#product of perpendiculars
e1=np.linalg.norm(e@F1-1)
print(e1)
e2=np.linalg.norm(e@F2-1)
print(e2)
e3=np.linalg.norm(e)**2
print(e3)
n=round(e1*e2/e3)
print(n)
len=100

theta=np.linspace(0,2*np.pi,len)
y=np.zeros((2,len))

y[0,:]=a*np.cos(theta)
y[1,:]=b*np.sin(theta)
plt.plot(y[0,:],y[1,:],label="Ellipse")
plt.plot(F1[0],F1[1],'o')
plt.text(F1[0]*(1+0.1),F1[1]*(1-0.1),'F1')
plt.plot(F2[0],F2[1],'o')
plt.text(F2[0]*(1+0.1),F2[1]*(1-0.1),'F2')
m=omat@e
A_1=y_icept(e,c1)
x_tangent=line_dir_pt(m,A_1,1.5,20)
plt.plot(x_tangent[0,:],x_tangent[1,:],label="Tangent")
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1),P[1]*(1),'P')
plt.title('conics1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.grid()
plt.axis('equal')
plt.show()