# Fall 1: List Comprehension
x = 100                          # x ist GLOBAL, Wert = 100
lst = [x for x in range(3)]     # neues x NUR für die Comprehension
print(x)                         # welches x? → das GLOBALE → 100

# Das x in [x for x in range(3)] ist eine komplett eigene Variable, die nur innerhalb der eckigen Klammern existiert. Sie hat zufällig denselben Namen wie das globale x, aber sie ist eine andere. Nach der Comprehension ist sie weg. Das globale x = 100 wurde nie angefasst.
# → print(x) gibt 100 aus.

# Fall 2: for-Schleife
x = 100  # x ist global =100
lst =[]
for x in range(3): # Schleife benutzt globales x
    lst.append(x)  # Erstellt x=0, 1, 2 und stoppt dann
print(x)           # x = 2, da es von der Schleife überschrieben wurde
