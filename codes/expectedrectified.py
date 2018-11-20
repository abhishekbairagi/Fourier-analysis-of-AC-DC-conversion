import numpy as np
import matplotlib.pyplot as plt 

A = 16
x = np.linspace(-0.01*np.pi, 0.01*np.pi,100000)

y = np.absolute(A*np.sin(2*np.pi*50*x))

plt.plot(x,y)
plt.ylabel("Rectified Output")
plt.xlim(-0.01*np.pi, 0.01*np.pi)
plt.xlabel("Time")
plt.grid()
plt.show()