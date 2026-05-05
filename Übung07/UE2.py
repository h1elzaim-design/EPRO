numbers = [1, 2, 2, 3, 4, 4, 5, 6]
for n in numbers[:]: #Fehler war dass aus der originalen Liste gelöscht wurde und Python dadurch einige Elemente übersprungen hat
    if n % 2 == 0:
        numbers.remove(n)
print(numbers)
