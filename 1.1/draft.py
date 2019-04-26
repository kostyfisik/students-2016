import numpy as np
import matplotlib.pyplot as plt
from numba import jit


#points
a = 11  #X border
b = 1  #Y border
N = 101 #X Size
M = 101  #Y Size


#J - iters
iters = 120

#mesh & u arr
[X, Y] = np.meshgrid(np.linspace(0,a,N),np.linspace(0,b,M))
u_p = np.zeros([M,N])
u = np.zeros([M,N])

Cc = ((X[0,1] - X[0,0])/(Y[1,0] - Y[0,0]))**2   #coords const

#boundary conditions
u[M-1,:] = np.sin(X[0,:])/np.sin(a)
u[:,N-1] = np.sinh(Y[:,0])/np.sinh(b)



Err = np.zeros(iters)

#Start:
for Jc in range(iters):
    u_p[:] = u[:]
    for i in range(1, N-1):
        for j in range(1, M-1):
            u[j,i] = (Cc*(u_p[j-1,i]+u_p[j+1,i])+u_p[j,i-1]+u_p[j,i+1])/(2*(1+Cc))
    Err[Jc] = np.max(np.abs(u-u_p))
    
fig, ax = plt.subplots()
ax.plot(Err)

fig, ax = plt.subplots()
cax = ax.contourf(X,Y,u,100)
fig.colorbar(cax)