def merge(left: list, right: list) -> list: 
    result = []
    i,y = 0, 0
    while i < len(left) and y < len(right): 
        if left[i] <= right[y]: 
            result.append(left[i])
            i += 1
        else: 
            result.append(right[y])
            y += 1
    result.extend(left[i:])
    result.extend(right[y:])
    return result

print(merge([1, 3, 5, 7, 10, 13], [2, 4, 6, 8, 9, 11, 12, 14, 15]))
    