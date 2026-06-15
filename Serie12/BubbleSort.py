import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

times = []
ns = [2**k for k in range(1, 13)]

for n in ns:
    arr = [random.random() for _ in range(n)]      # zufällige Liste der Länge n
    start = time.time()
    bubble_sort(arr)
    end = time.time()
    times.append(end - start)

plt.loglog(ns, times, label='bubble sort')
plt.loglog(ns, [2e-8 * n**2 for n in ns], label='O(n²)', linestyle='dashed')
plt.xlabel('n')
plt.ylabel('Zeit (s)')
plt.legend()
plt.show()