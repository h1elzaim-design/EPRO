import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2                         
x0, y0 = -4, 4
T = (x0**2 + y0**2) + (2*x0) * (X - x0) + (2*y0) * (Y-y0)                    

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=11, azim=-140)
ax.set_zlim(-20, 60)
ax.plot_surface(X, Y, Z, alpha=0.7, label='f(x,y)')
ax.plot_surface(X, Y, T, alpha=0.5, label='Tangentialebene')
ax.plot([-4, -4], [4, 4], [-150, 32], color='red', linewidth=2, label='Berührpunkt')
ax.set_title('Tangentialebene')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()