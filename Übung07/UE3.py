def flatten(lst):
    result = []
    for i in lst:
        for j in i:
            result.append(j)
    return result 

print(flatten([[1,2,3], [4,5,6], [7,8,9]])) 
        
