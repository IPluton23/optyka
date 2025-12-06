import numpy as np
import matplotlib.pyplot as plt

x_c, z_c=0,0
R=5
w=2
size=16

z=np.linspace(-w/2, w/2, 500)
x_upper=x_c+np.sqrt(R**2 - z**2)-(R-w/2)
x_lower=x_c-(np.sqrt(R**2 - z**2)+(R-w/2))


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