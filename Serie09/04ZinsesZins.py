def rich_when(start_money, interest, deposit, lvl_of_rich=1000000):
    kapital = start_money
    year = 0
    while kapital < lvl_of_rich:
        kapital = kapital * (1 + interest/100) + deposit
        year += 1
    return year

print(rich_when(10000, 10, 5000)) 
print(rich_when(10000, 9, 5000))
print(rich_when(10000, 8, 5000))
print(rich_when(10000, 7, 5000))
print(rich_when(10000, 6, 5000))
 