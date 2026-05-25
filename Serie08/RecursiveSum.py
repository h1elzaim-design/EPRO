def nested_sum(lst):
    sum = 0
    if isinstance(lst, list):
        for i in lst:
            sum += nested_sum(i)
    else:
        sum += lst
    return sum

print(nested_sum([1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]]))