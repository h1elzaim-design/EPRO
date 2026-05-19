''' Eine Funktion die eine Liste aller Primes bis n ausgibt '''



def eratosthenes(n):
    numbers = list(range(2, n + 1))
    i = 0
    while i < len(numbers):
        prime = numbers[i]
        numbers = [num for num in numbers if num % prime != 0 or num == prime]
        i += 1
    return numbers


print(eratosthenes(17))


        