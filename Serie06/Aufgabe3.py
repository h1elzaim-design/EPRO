n =12345

# Weg 1: for-Schleife
summe = 0
for ziffer in str(n):
    summe += int(ziffer)
print(summe)

# str(n) machte aus der Zahl einen String
# for-Schleife iteriert über jeden Buchstaben "1",...
# mit int(ziffer), wird jeder Buchstabe wieder zu einer Zahl
# summe += int(ziffer) addiert die Zahl zur Summe

# Weg 2: list-comprehension
summe = sum([int(z) for z in str(n)])
print(summe)

# Weg 3: map

summe = sum(map(int, str(n))) # map wendet eine Funktion auf jedes Element an
print(summe)