import math

N = int(input("Anzahl Personen: "))

P = 1 - math.factorial(365) / (365**N * math.factorial(365 - N))
print(f"Wahrscheinlichkeit: {P:.4f}")