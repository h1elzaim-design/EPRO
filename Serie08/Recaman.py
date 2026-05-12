def recaman_iter(n):
    seen = set()
    a = 0
    seen.add(0)
    for i in range(1, n+1):
        if a-i > 0 and (a-i) not in seen:
            a = a-i
        else:
            a = a+i
        seen.add(a)
    return a

print(recaman_iter(1000))

def recaman_rec(n, seen=None):
    if seen is None:
        seen = set()
    if n == 0:
        seen.add(0)
        return 0
    prev = recaman_rec(n-1, seen)
    if prev - n > 0 and (prev - n) not in seen:
        result = prev - n
    else: 
        result = prev + n
    seen.add(result)
    return result


print(recaman_rec(1000))