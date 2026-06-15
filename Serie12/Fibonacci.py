import numpy as np
import time
import matplotlib.pyplot as plt

def fib_rekursiv(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_rekursiv(n-1) + fib_rekursiv(n-2)

def fib_iterativ(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    for k in range(1, n):
        a, b = b, a + b
    return b

def fib_matrix(n):
    if n == 0:
        return 0
    A = np.array([[1, 1], [1, 0]])
    M = np.linalg.matrix_power(A, n)
    return M[0, 1]

ns_recursive = list(range(1,25))
ns_iter_mat = [2**k for k in range(1, 20)]

times_recursive = []
times_iterative = []
times_matrix = []

for n in ns_recursive:
    start = time.time()
    fib_rekursiv(n)
    end = time.time()
    times_recursive.append(end - start)

for n in ns_iter_mat:
    start = time.time()
    fib_iterativ(n)
    end = time.time()
    times_iterative.append(end - start)

for n in ns_iter_mat:
    start = time.time()
    fib_matrix(n)
    end = time.time()
    times_matrix.append(end - start)

plt.loglog(ns_recursive, times_recursive, label='rekursiv')
plt.loglog(ns_iter_mat, times_iterative, label='iterativ')
plt.loglog(ns_iter_mat, times_matrix, label='matrix')
plt.xlabel('n')
plt.ylabel('Zeit(s)')
plt.legend()
plt.show()