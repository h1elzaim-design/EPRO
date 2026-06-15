import time
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

def poly_direct(a, x):
    f_x = 0
    for n in range(len(a)):
        f_x += a[n] * x**n
    return f_x 

def poly_lookup(a, x):
    f_x = 0
    potenz = 1
    for k in range(len(a)):
        f_x += a[k] * potenz
        potenz = potenz * x 
    return f_x 

def poly_horner(a, x):
    f_x = a[-1]
    for n in range(len(a)-2, -1, -1):
        f_x = a[n] + x * f_x 
    return f_x

from functools import reduce

def poly_reduce(a, x):
    return reduce(lambda acc, a: acc * x + a, reversed(a))


ns = [2**k for k in range(1, 13)]
times_direct = []
times_lookup = []
times_horner = []
times_numpy = []
times_reduce = []
x = np.random.uniform(-1, 1, 10000)

for n in ns:
    a = np.random.uniform(-1, 1, n+1)

    start = time.time()
    poly_reduce(a, x)
    end = time.time()
    times_reduce.append(end - start)
    
    start = time.time()
    poly_direct(a, x)
    end = time.time()
    times_direct.append(end - start)

    start = time.time()
    poly_lookup(a, x)
    end = time.time()
    times_lookup.append(end - start)

    start = time.time()
    poly_horner(a, x)
    end = time.time()
    times_horner.append(end -start)

    start = time.time()
    np.polyval(a, x)
    end = time.time()
    times_numpy.append(end - start)

plt.loglog(ns, times_direct, label='direct')
plt.loglog(ns, times_lookup, label='lookup')
plt.loglog(ns, times_horner, label='horner')
plt.loglog(ns, times_numpy,  label='numpy')
plt.loglog(ns, times_reduce, label='reduce')
plt.xlabel('n')
plt.ylabel('Zeit (s)')
plt.legend()
plt.show()

