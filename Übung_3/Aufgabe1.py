m = int(input("Erste Zahl: "))
n = int(input("Zweite Zahl: "))

kleiner = min(m, n)
groesser = max(m, n)

if groesser % kleiner == 0:
    print(kleiner, "ist ein Teiler von", groesser)
else:
    print(kleiner, "ist kein Teiler von", groesser)