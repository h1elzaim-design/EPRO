A = [1, 2, 3, 4, 5]
B = [1, 3, 5, 4, 5]
result = [(a,b) for a, b in zip(A,B) if a != b]

print(result)