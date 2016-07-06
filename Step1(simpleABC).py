import numpy as np
import matplotlib.pyplot as plt
from math import exp
N=100 # walls position -N и N
eps=1 #epsilon
mu=1 #mue
Time=115 #moment of time
trange=500 #time range
t=0 #time moment for Gaussian
tdelay=20 #time delay for Gaussian
sigma=5 #Gaussian parametr
E=np.zeros(2*N+1) #electric field
H=np.zeros(2*N+1) #magnetic field
z=np.zeros(2*N+1) #position
#E[2*N]=0 # Electric wall PEC
#H[0]=0 # Magnetic wall PMC
a=0
b=0
c=0
f=0
g=0
h=0
for i in range (0,2*N+1):
    z[i]=i #position
######MAIN PART####
for t in range (0, Time+1):
    t1=E[2*N-1]
    t2=E[1]
    for k in range (1, 2*N+1):
        H[k]=H[k]+1/mu*(E[k]-E[k-1]) #TM mode
    #a=b
    #b=c
    #c=E[2*N]
    #H[1]=H[0]
    #E[N]=E[N]+exp(-(t-tdelay)*(t-tdelay)/(sigma*sigma)) #Source in the center
    for k in range (2*N-1, -1,-1):
        E[k]=E[k]+1/eps*(H[k+1]-H[k])
    #f=g
    #g=h
    #h=H[0]
    #E[2*N]=E[2*N-1]
    E[N]=E[N]+exp(-(t-tdelay)*(t-tdelay)/(sigma*sigma)) #Source in the center
    E[2*N]=t1 #Field reassignment Simple ABC
    #H[2*N]=H[2*N-1]
    #H[0]=H[1] #Field reassignment
    E[0]=t2
    if t==Time:
        print(E)
        print(H)
        plt.figure(1)
        plt.subplot(211)
        plt.plot(z, E, 'k--')
        plt.xlabel('coordinate')
        plt.ylabel('E-field')
        #plt.axis([0, 2*N+1, -1, 1])

        plt.subplot(212)
        plt.plot(z, H, 'r--')
        plt.xlabel('coordinate')
        plt.ylabel('H-field')
        #plt.axis([0, 2*N+1, -1, 1])
        plt.show()
        #plt.plot(z,E)
        #plt.plot(z,H)
        plt.show()

