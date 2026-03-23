import random

wurf1 = random.randint(1, 20)
wurf2 = random.randint(1, 20)
ergebnis = max(wurf1, wurf2)

if ergebnis == 20:
    print("20, ein kritischer Treffer!")
else:
    print(ergebnis)