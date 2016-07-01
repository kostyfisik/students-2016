import numpy as np
import matplotlib.pyplot as plt
from math import exp
N=150 # walls position -N и N
eps=1 #epsilon
mu=1 #mue
Time=200 #moment of time
trange=500 #time range
t=0 #time moment for Gaussian
tdelay=50 #time delay for Gaussian
sigma=10 #Gaussian parametr
E=np.zeros(2*N+1) #electric field
H=np.zeros(2*N+1) #magnetic field
z=np.zeros(2*N+1) #position
E[2*N]=0 # Electric wall PEC
H[0]=0 # Magnetic wall PMC
for i in range (0,2*N+1):
    z[i]=i #position
######MAIN PART####
for t in range (0, trange):
    for k in range (1, 2*N+1):
        H[k]=H[k]+1/mu*(E[k]-E[k-1])  
    E[N]=E[N]+exp(-(t-tdelay)*(t-tdelay)/(sigma*sigma)) #Source in the center
    for k in range (0, 2*N):
        E[k]=E[k]+1/eps*(H[k+1]-H[k]) 
    #E[N+1]=E[N+1]+exp(-(t-tdelay)*(t-tdelay)/(sigma*sigma)) #Source in the center
    if t==Time:
        print(E)
        print(H)
        plt.plot(z,E)
        plt.plot(z,H)
        plt.show()

