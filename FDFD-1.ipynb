%matplotlib inline 

import numpy as np
import math as math
import matplotlib.pyplot as plt
import scipy as sp 
import scipy.sparse.linalg as ssl

a = 1 #domain size
n = 100 #number of grid nodes
dz = a/n #discretization unit
#c = 3*10**8 #light velosity
B = np.zeros((n,n))
F = np.zeros((n,n))

for number in range(n):
    B[number,number] = 1
    F[number,number] = -1
for number in range(n-1):
    B[number+1,number] = -1
    F[number,number+1] = 1
B = B/dz
F = F/dz
q = -B*F

kt = 2*sp.pi*a # wave vector target to find resonance wavelength
k2, V = ssl.eigs(q, k=6, M=None, sigma=kt**2) 
#print(k2)
#print(V)

k = np.real(np.sqrt(k2)); # resonance wave vector 

print(k)
#print(q)
#print(q)
#print(np.linalg.det(q))

#A=1/(c^2)*np.eye(n)

#eigenmodes = np.linalg.solve(A,q)
#print(eigenmodes)

#v,w = np.linalg.eig(q)
#print(v)
#print(w)

lam = 2*sp.pi/np.real(k); # wavelength
Q = np.real(k)/(2*np.imag(k)); # quality factor

plt.hold(True)
plt.plot(np.arange(1,6.1,1), lam, '-')
plt.plot(np.arange(1,6.1,1), 4/(2*np.arange(0,5.1,1)+1), '*')

f, ax = plt.subplots(6,1, sharex=True, sharey=True)
for nOfInd in range(6):
    ax[nOfInd].plot(V[:,nOfInd],'-')



tau=100.0 #width of the puls
t0=10.0*tau #delay of the source
tot_time=int(n+t0)
source_point=n//2

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

#for q in range(tot_time):
#    for m in range(n-1):
#        hy[m]+=(ex[m+1]-ex[m])
#    for m in range(n-1):
#        ex[m+1]+=(hy[m+1]-hy[m])
#        if m==source_point:
#            ex[m]+=source(q,t0,tau)
#    if q % int(n/10)==0 or q+5>tot_time:
#        drawplot(z, ex, hy, q)
