"""
Aufgabe 4: Monte-Carlo-Simulation (Würfel)
"""

import random

def mc_mean(n, N=1000):
    """Simuliert N-mal das Würfeln mit n 6-seitigen Würfeln
    und gibt den Durchschnitt der Summen zurück.
    
    Erwartungswert: 3.5 * n
    """
    total = 0
    for _ in range(N):
        wurf_summe = sum(random.randint(1, 6) for _ in range(n))
        total += wurf_summe
    return total / N


if __name__ == "__main__":
    for n_dice in [1, 2, 5]:
        result = mc_mean(n_dice, N=100000)
        expected = 3.5 * n_dice
        print(f"n={n_dice}: mc_mean = {result:.4f}  (Erwartungswert: {expected})")
