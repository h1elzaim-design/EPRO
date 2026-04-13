A = input("Wort A: ")
B = input("Wort B: ")
vokale = "aeiou"

vokale_a = {c for c in A.lower() if c in vokale}
vokale_b = {c for c in B.lower() if c in vokale}

print("Positives Ergebnis" if vokale_a == vokale_b else "Negatives Ergebnis")