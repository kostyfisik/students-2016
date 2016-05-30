%matplotlib inline 

import numpy as np
import math as math
import matplotlib.pyplot as plt

n = 5000 #number of points
tau = 100.0 #puls width
t0 = 10.0*tau #delay of the source
tot_time = int(n+t0)
source_point = n//2

pml_width=5 #PML width
eps = 25*np.ones(n)

dx = 1
R0 = 10**(-6)
m = 1
  
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
    plt.savefig("step1-at-time-%i.png"%q, fmt='png')
    plt.draw()

ex=np.zeros(n)
hy=np.zeros(n)
z=np.linspace(0,n-1,n)

Smax = -(m+1)*np.log(R0)/2/(pml_width*dx)
Se = np.zeros(n)
Sm = np.zeros(n)

for mm in range(int(pml_width)):
    Se[mm+1] = Smax*((pml_width-mm-0.5)/pml_width)**m
    Sm[mm] = Smax*((pml_width-mm)/pml_width)**m
    Se[n-mm-1] = Smax*((pml_width-mm-0.5)/pml_width)**m  
    Sm[n-mm-1] = Smax*((pml_width-mm)/pml_width)**m
    
Ae = np.exp(-Se)
Be = np.exp(-Se) + 1
Am = np.exp(-Sm)
Bm = np.exp(-Sm) + 1

Pm = np.zeros(n)
Pe = np.zeros(n)

for q in range(tot_time):
    for nn in range(n-1):
        Pm[nn] = Bm[nn]*Pm[nn] + Am[nn]*(ex[nn+1] - ex[nn])
        hy[nn] += ex[nn+1] - ex[nn] + Pm[nn]
    for nn in range(n-1):
        Pe[nn+1] = Be[nn+1]*Pe[nn+1] + Ae[nn+1]*(hy[nn+1] - hy[nn])
        ex[nn+1] += (hy[nn+1] - hy[nn])/eps[nn] + Pe[nn+1]/eps[nn]
        if nn==source_point:
            ex[nn] += source(q,t0,tau)           
    if q % int(n/10)==0 or q+5>tot_time:
        drawplot(z, ex, hy, q)
