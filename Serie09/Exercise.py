import random
import string

# ── Runde 1 ──────────────────────────────────────────────────
def häufigster_würfel(n):
    zähler = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for _ in range(n):
        wurf = random.randint(1, 6)
        zähler[wurf] += 1
    return max(zähler, key=zähler.get)

def primzahl_summe(n):
    return sum(eratosthenes(n))

def verdoppeln(start, ziel):
    count = 0
    while start < ziel:
        start = start * 2
        count += 1
    return count

def einzel_lotto():
    randoms = set()
    while len(randoms) < 6:
        randoms.add(random.randint(1, 45))
    return list(randoms)

# ── Runde 2 ──────────────────────────────────────────────────
def münzwurf(n):
    kopf = 0
    for _ in range(n):
        wurf = random.randint(0, 1)
        if wurf == 0:
            kopf += 1
    return kopf

def max_prime_after(n):
    primes = eratosthenes(n + 100)
    for p in primes:
        if p > n:
            return p

def pw_generator(länge):
    pw = ""
    for _ in range(länge):
        pw += random.choice(string.ascii_lowercase)
    return pw

# ── Runde 3 ──────────────────────────────────────────────────
def sum_gerade(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum += i
    return sum

def countdown(n):
    liste = []
    for i in range(n, -1, -1):
        liste.append(i)
    return liste

def würfel_bis_sechs():
    würfe = 0
    wurf = 0
    while wurf != 6:
        wurf = random.randint(1,6)
        würfe += 1
    return würfe

def kehre_um(text):
    ergebnis = ""
    for i in range(len(text)-1,-1,-1):
        ergebnis += text[i]
    return ergebnis
