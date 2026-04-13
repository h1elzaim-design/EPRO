import random
A = [random.randint(1,100)
for _ in range(100)]
mittelwert = sum(A)/len(A)
sortiert = sorted(A)
mitte = len(sortiert)//2
median = (sortiert[mitte - 1]+sortiert[mitte])/2
über = len([x for x in A if x>mittelwert])
unter = len([x for x in A if x<mittelwert])

print(f"Mittelwert: {mittelwert}")
print(f"Median: {median}")
print(f"Größer als Mittelwert: {über}")
print(f"Kleiner als Mittelwert: {unter}")