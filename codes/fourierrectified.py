import numpy as np
import matplotlib.pyplot as plt
import cmath


T_0 = 0.01                                     # defining amplitude, frequency, no. of terms 
T = 0.02
f = 1/T
A = 16      
r = 100
g = 0

t = np.linspace(-0.01*np.pi, 0.01*np.pi,100000)

for n in range(-r,r):
	if n == 0:
		g = g +  2.0*A/np.pi;
	else:
		print n
		an = (-2.0*A/np.pi)*(1.0/(4*n*n-1))    # finding an for each n
		cos = np.cos(n*2*np.pi*f*t)
		g = g + an*cos                         # adding the fourier series terms


plt.plot(t,g)                                  # plotting the output
plt.grid ()
plt.xlabel('$t$')
plt.xlim(-0.01*np.pi,0.01*np.pi)
plt.ylabel('$Rectified sine wave$')
plt.show()