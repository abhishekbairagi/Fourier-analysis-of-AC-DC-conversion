import numpy as np
import matplotlib.pyplot as plt
import cmath

T_0 = 0.01                                     # defining amplitude, frequency, no. of terms 
T = 0.02
f = 1/T
A = 16      
r = 20
g = 0
an = []
no = np.linspace(-r, r,2*r )
for n in range(-r,r):
	if n == 0:
		an.append(2.0*A/np.pi)
	else:
		print n
		x =(-2.0*A/np.pi)*(1.0/(4*n*n-1))
		an.append(x)    # finding an for each n
		                        # adding the fourier series terms


plt.plot(no,an,'.')                                # plotting the output
plt.grid ()
plt.xlabel('$t$')
#plt.xlim(-r-1,r+1)
plt.ylabel('$Rectified sine wave$')


R = 10
C = 10**(-3)
t= np.linspace(-2.5*T, 2.5*T, 1e4)
f = np.linspace(-100 , 100 , 1e6)
h = 1/((1j*R*C*2*np.pi*f) + 1)
plt.plot(f, h)
plt.show()
