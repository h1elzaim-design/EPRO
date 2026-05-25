import numpy as np
import matplotlib.pyplot as plt
def mandelbrot(z: complex, upperlim: int = 30) -> int:
    a = 0
    for n in range(upperlim):
        if abs(a) > 2:
            return n
        a = a**2 + z
    return upperlim

nx = 1000 # take nx many points in x-direction
ny = 1000 # take ny many points in y-direction for z = x + iy
x = np.linspace(-2, 0.5, nx)
y = np.linspace(-1, 1, ny)
F = np.empty((ny, nx), dtype=float)
for i, yy in enumerate(y):
    for k, xx in enumerate(x):
        z = xx + 1j * yy
        F[i, k] = mandelbrot(z)
X, Y = np.meshgrid(x, y)
plt.pcolormesh(X, Y, F)
plt.show()
