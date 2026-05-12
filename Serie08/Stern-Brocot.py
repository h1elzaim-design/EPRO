import matplotlib.pyplot as plt

def stern(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1   # definiere die ersten beiden Werte
    if n % 2 == 0:
        return stern(n // 2) # wenn n gerade ist, halbiere den Index
    else:
        return stern(n // 2 + 1) + stern(n // 2) # wenn n ungerade ist addiere die beiden Hälften

#############################
#       Visualization       #
#############################
N = 10000

# Plot values a_n over index n
xs = list(range(N + 1))
ys = [stern(n) for n in xs]

plt.figure(figsize=(10, 4))
plt.scatter(xs, ys, s=5)
plt.xlabel("n")
plt.ylabel("a_n")
plt.show()

# Plot values a_n / a_{n-1} over index n
ratios = [stern(n) / stern(n-1) for n in range(2, N + 1)]
indices = list(range(2, N + 1))

plt.figure(figsize=(12, 4))
plt.scatter(indices, ratios, s=5)
plt.xlabel("n")
plt.ylabel("a_n / a_{n-1}")
plt.show()