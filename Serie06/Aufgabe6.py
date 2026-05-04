def sus_only(transactions, limit = 4200):
    return [t for t in transactions if t > limit]    


transactions = [100, 200, 4000, 5000, 600, 7000, 8000, 9000, 10000]

print(sus_only(transactions))
