darstellbar = {6*a + 8*b + 9*c + 10*d + 20*e 
    for a in range(34)
    for b in range(26)
    for c in range(23)
    for d in range(21)
    for e in range(11)
    if 6*a +8*b + 9*c + 10*d + 20*e <=200}
print(max({x for x in range(1,201) if x not in darstellbar}))

