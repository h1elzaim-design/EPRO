M = [[0,1,2],[3,4,5],[6,7,8]]

def reverse_rows_ref(M):
    return M[::-1] # dreht M um


print(reverse_rows_ref(M))

import copy

def reverse_rows_deep(M):
    return copy.deepcopy(M)[::-1]


print(reverse_rows_deep(M))

# Test
    #Var1: 
ref = reverse_rows_ref(M)
ref[0] .append(100)
print(M)

# M resetten
M = [[0,1,2],[3,4,5],[6,7,8]]

    #Var2: 
deep = reverse_rows_deep(M)
deep[0].append(100)
print(M) 
