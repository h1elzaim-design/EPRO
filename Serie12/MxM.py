import time
import numpy as np
import matplotlib.pyplot as plt

times = []
ns = [2**k for k in range(1, 9)]  # kleinere ns weil Matrizen viel größer sind

for n in ns:
    A = np.random.random((n, n))  # zufällige n×n Matrix
    B = np.random.random((n, n))  # zufällige n×n Matrix
    start = time.time()
    M = A @ B   # Matrix-Matrix-Multiplikation
    end = time.time()
    times.append(end - start)

plt.loglog(ns, times, label='A @ B')
plt.loglog(ns, [1e-9 * n**3 for n in ns], label='O(n³)', linestyle='dashed')
plt.xlabel('n')
plt.ylabel('Zeit (s)')
plt.legend()
plt.show()