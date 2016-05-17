%matplotlib inline 

import numpy as np
import math as math
import matplotlib.pyplot as plt

n=5000 #number of points
tau=100.0 #puls width
t0=10.0*tau #delay of the source
tot_time=int(n+t0)
source_point=n//2
pml_width=5 #PML width
sigma_eps = 10**3 
sigma_mu = 10**3 
eps = 5
mu = 1
delta = 1/n #step width
eta1_eps = (2*eps-sigma_eps*delta)/(2*eps+sigma_eps*delta)
eta1_mu = (2*mu-sigma_mu*delta)/(2*mu+sigma_mu*delta)
eta2_eps = 1/(2*eps+sigma_eps*delta)
eta2_mu = 1/(2*mu+sigma_mu*delta)

def source(t, t0, tau):
    return math.exp(-(t-t0)**2/(2.0 * tau**2))

def drawplot(z, ex, hy, q):
    fig = plt.figure()
    plt.title("After t=%i"%q)
    plt.grid(True)
    plt.xlabel(u'Coordinate z')
    plt.ylabel(u'Function')
    ax = fig.add_subplot(211)
    ax.plot(z, ex, '-', color='blue', linewidth=2, label=u'Ex')
    ax.plot(z, hy, '--', color='red', linewidth=2, label=u'Hy')
    bx = fig.add_subplot(212)
    bx.plot(z, ex, '-', color='blue', linewidth=2, label=u'Ex')
    plt.savefig("step0-at-time-%i.png"%q, fmt='png')
    plt.draw()

ex=np.zeros(n)
hy=np.zeros(n)
z=np.linspace(0,n-1,n)

for q in range(tot_time):
    for m in range(n-1-pml_width):
        hy[m]+=(ex[m+1]-ex[m])
    for m in range(n-1-pml_width,n-1):
        hy[m]=eta1_mu*hy[m] + eta2_mu*(ex[m+1]-ex[m])
    ex[0]=ex[1]
    for m in range(n-1-pml_width):
        ex[m+1]+=(hy[m+1]-hy[m])
        if m==source_point:
            ex[m]+=source(q,t0,tau)
    for m in range(n-1-pml_width,n-1):
        ex[m+1] = eta1_eps*ex[m+1] + eta2_eps*(hy[m+1]-hy[m])
    if q % int(n/10)==0 or q+5>tot_time:
        drawplot(z, ex, hy, q)
