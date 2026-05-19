def collatz(k):
    a = k
    count = 0
    while a != 1:
        if a % 2 == 0:
            a = a/2
            count += 1
        else:
            a = 3*a+1
            count += 1
    return count
