def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    result = 0
    for j in range(n): # geh durch jede Spalte in der ersten Zeile
        sign = (-1) ** j 
        sub = [row[:j] + row [j+1:] for row in A[1:]]  
        result += sign * A[0][j] * det(sub)
    return result

print(det([[1,2,3],[4,5,6],[7,8,9]])) 
print(det([[1,2],[3,4]]))