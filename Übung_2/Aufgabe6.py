n = int(input("Zahl n: "))
reihen = int(input("Anzahl der Reihen: "))

zeile1 = "O " * n + "\n"
zeile2 = " O" * n + "\n"
paar = zeile1 + zeile2

print(paar * (reihen // 2) + zeile1 * (reihen % 2))

