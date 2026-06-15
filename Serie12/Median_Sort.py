import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quicksort_m3(arr):
    if len(arr) <= 2:
        return sorted(arr)
    mid = len(arr) // 2
    pivot = sorted([arr[mid-1], arr[mid], arr[mid+1]])[1]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quicksort_m3(left) + middle + quicksort_m3(right)

ns = [2**k for k in range(1, 13)]
times_bubble = []
times_quick  = []

for n in ns:
    arr = [random.random() for _ in range(n)]
    
    start = time.time()
    bubble_sort(arr[:])      # arr[:] damit bubble_sort eine Kopie bekommt
    end = time.time()
    times_bubble.append(end - start)

    start = time.time()
    quicksort_m3(arr)
    end = time.time()
    times_quick.append(end - start)

plt.loglog(ns, times_bubble, label='bubble sort')
plt.loglog(ns, times_quick,  label='median-of-3 quicksort')
plt.loglog(ns, [1e-7  * n    for n in ns], label='O(n)',  linestyle='dashed')
plt.loglog(ns, [2e-8  * n**2 for n in ns], label='O(n²)', linestyle='dashed')
plt.xlabel('n')
plt.ylabel('Zeit (s)')
plt.legend()
plt.show()