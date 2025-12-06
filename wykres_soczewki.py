import numpy as np
import matplotlib.pyplot as plt

x_c1, z_c = 0,0     # koordynaty centrum sferY 1 (lewej)
x_c2 = 0            # koordynaty centrum sfery 2 (prawej), są na tej samej wysokości z_c
R = 5
wysokosc = 10       # wysokosc soczewki

size = 16           # szerokość wykresu


z = np.linspace(-wysokosc/2, wysokosc/2, 500)
x_upper = x_c1 + (np.sqrt(R**2 - z**2)-(R-wysokosc/2))      # Prawa część soczewki - pochodzi od sfery lewej
x_lower = x_c2 - (np.sqrt(R**2 - z**2)+(R-wysokosc/2))      # Lewa część soczewki


plt.figure(figsize=(6,6))
plt.fill_betweenx(z+z_c, x_lower, x_upper, color='skyblue')
plt.plot(x_upper, z+z_c)
plt.plot(x_lower, z+z_c)
plt.xlim(-size, size)
plt.ylim(-size, size)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('z')
plt.show()

