class MySet:
    def __init__(self, list):
        self.elements = []
        for element in list:
            if element not in self.elements:
                self.elements.append(element)
    
    def __add__(self, other):
        new = self.elements.copy()
        for element in other.elements:
            if element not in new:
                new.append(element)
        return MySet(new)

    def __sub__(self, other):
        new = []
        for element in self.elements:
            if element not in other.elements:
                new.append(element)
        return MySet(new)

    def add(self, a):
        if a not in self.elements:
            self.elements.append(a)




'''Test'''
'__init__'
s = MySet([1, 2, 2, 3, 3, 3])
print(s.elements)    # [1, 2, 3]

'__add__'
s1 = MySet([1, 2, 3])
s2 = MySet([2, 3, 4, 5])
s3 = s1 + s2
print(s3.elements)    # [1, 2, 3, 4, 5]  ← keine Duplikate!
'__sub__'
s1 = MySet([1, 2, 3, 4])
s2 = MySet([2, 3])
s3 = s1 - s2
print(s3.elements)    # [1, 4]  ← nur was in s1 aber NICHT in s2 ist
'add'
s = MySet([1, 2, 3])
s.add(4)
print(s.elements)    # [1, 2, 3, 4]

s.add(2)             # schon drin!
print(s.elements)    # [1, 2, 3, 4]  ← keine Duplikate