import random

def coupon_collector(n):
    gesammelt = set()
    anzahl = 0
    while len(gesammelt) < n:
        pickerl = random.randint(1, n) #random Pickerl
        gesammelt.add(pickerl) # Set ignoriert doppel
        anzahl += 1
    return anzahl

def messi_lover(n, num_iter):
    summe = sum(coupon_collector(n) for _ in range(num_iter))
    return summe / num_iter

print(messi_lover(10, 10000))
print(messi_lover(100, 10000))
print(messi_lover(1000, 1000)) 