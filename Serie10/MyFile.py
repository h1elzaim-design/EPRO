class MyFile:
    def __init__(self, liste):
        self.originale = []
        for original in liste:
            if original not in self.originale:
                self.originale.append(original)

    def __add__(self, other):
        addierte = self.originale.copy()
        for original in other.originale:
            if original not in addierte:
                addierte.append(original)
        return MyFile(addierte)

    def __sub__(self, other):
        subtrahierte = []
        for original in self.originale:
            if original not in other.originale:
                subtrahierte.append(original)
        return MyFile(subtrahierte)
    
    def add(self, a):
        if a not in self.originale:
            self.originale.append(a)



    '''Test'''
s1 = MyFile([1, 2, 2, 3])
print(s1.originale)              # [1, 2, 3]
s2 = MyFile([2, 3, 4])
print((s1 + s2).originale)       # [1, 2, 3, 4]
print((s1 - s2).originale)       # [1]
