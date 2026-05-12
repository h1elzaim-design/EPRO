def triangle_lists(n: int):
    triangle = []  #Fehler war die empty_list n mal in triangle eingefügt wurde - also immer in die selbe liste statt einer neuen.

    for _ in range(n): # erstellen der leeren Listen
        triangle.append([]) 

    for i in range(n): # i = 0, 1, 2
        for j in range(n-i): # j geht von 0 bis n-i durch
            triangle[j].append(i) # es wird i an der Position j angehängt
 
    return triangle

for row in triangle_lists(3): # jede innere liste wird einzeln ausgegeben 
    print(row)


