def back_substitution(U, b):
    n = len(b)
    x = [0] * n
    try:
        x[n-1] = b[n-1] / U[n-1][n-1]
    except ZeroDivisionError:
        print('Fehler: Division durch Null!')
        return None
    for i in range(n-2, -1, -1):
        summe = 0
        for j in range(i+1, n):
            summe += U[i][j] * x[j]
        try:
            x[i] = (b[i] - summe) / U[i][i]
        except ZeroDivisionError:
            print('Fehler: Division durch Null!')
            return None
    return x

    '''Test'''
U = [[2, 3, 1],
     [0, 4, 2],
     [0, 0, 3]]
b = [9, 8, 6]

print(back_substitution(U, b))    # [2.0, 1.0, 2.0]