def flat(lst):
    result = []
    for item in lst:
        if isinstance(item,list): #prüfe ob das Element in der Liste ist
            result.extend(flat(item)) #wenn ja, rufe die Funktion erneut auf
        else:
            result.append(item) #wenn nein, füge es zur Ergebnisliste hinzu
    return result

print(flat([1, [2, 3], 4, [5, [6, 7]]]))

