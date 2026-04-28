"""
Aufgabe 1: Primzahlen
"""

def primes1(n):
    """Gibt alle Primzahlen <= n als Liste zurück (ohne Module)."""
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# Bonus
def primes2(n):
    """Gibt die ersten n Primzahlen als Liste zurück."""
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(candidate**0.5) + 1):
            if candidate % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes


if __name__ == "__main__":
    print(f"primes1(20) = {primes1(20)}")
    print(f"primes2(8)  = {primes2(8)}")
