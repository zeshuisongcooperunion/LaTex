import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,1000)
y = np.sin(x)/x

plt.plot(x,y)
plt.grid()
plt.show()