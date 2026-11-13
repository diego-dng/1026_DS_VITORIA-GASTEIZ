import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = x+2
z = x+5
# fig = plt.figure()
fig = plt.figure()
plt.plot(x, x, '-')
plt.plot(x, y, '--')
plt.plot(x, z, '.')

fig.savefig('img/figure_prueba.jpg')