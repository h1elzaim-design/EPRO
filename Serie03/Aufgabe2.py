n = int(input("Jahreszahl: "))

if n % 400 == 0:
    print(n, "ist ein Schaltjahr")
elif n % 100 == 0:
    print(n, "ist kein Schaltjahr")
elif n % 4 == 0:
    print(n, "ist ein Schaltjahr")
else:
    print(n, "ist kein Schaltjahr")
    