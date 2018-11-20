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
		an.append(x)                           # an is list for amplitudes
		                        


plt.plot(no,an,'.')                                # plotting the output
plt.grid ()
plt.xlabel('$f$')
plt.xlim(-r-1,r+1)
plt.ylabel('$Amplitudes$')
plt.show()