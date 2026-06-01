class Polynom:
    def __init__(self, koeff):
        self.koeff = koeff
        self.grad = len(koeff) - 1

    def eval(self, x):
        ergebnis = 0
        for i, a in enumerate(self.koeff):
            ergebnis += a * x**i
        return ergebnis

    def deriv(self):
        if self.grad == 0:
            return Polynom([0])
        neue = [i * self.koeff[i] for i in range(1, self.grad + 1)]
        return Polynom(neue)

    def zeros(self):
        if self.grad != 2:
            raise ValueError('Nur für Polynome 2.Grades')
        a = self.koeff[2]
        b = self.koeff[1]
        c = self.koeff[0]
        disk = b**2 - 4*a*c
        if disk < 0:
            return None
        x1 = (-b + disk**0.5)/(2*a)
        x2 = (-b - disk**0.5)/(2*a)
        return (x1, x2)

    def __add__(self, other):        
        n = max(len(self.koeff), len(other.koeff))
        fill_a = self.koeff + [0] * (n - len(self.koeff))
        fill_b = other.koeff + [0] * (n - len(other.koeff))
        return Polynom([fill_a[i] + fill_b[i] for i in range(n)])
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                return Polynom([0])    
            return Polynom([a * other for a in self.koeff])
            
        
        elif isinstance(other, Polynom):
            c = [0] * (self.grad + other.grad  + 1)
            for i in range(self.grad + 1):
                for j in range(other.grad + 1):
                    c[i+j] += self.koeff[i] * other.koeff[j]
            return Polynom(c)
    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        terms = []
        for i, a in enumerate(self.koeff):
            if a == 0: 
                continue
            if i == 0:
                terms.append(str(a))
            elif i == 1:
                terms.append(f'{a}x')
            else:
                terms.append(f'{a}x^{i}')
        return ' + '.join(terms)if terms else '0'
    
    def __le__(self, other):
        if self.grad != other.grad:
            return self.grad <= other.grad
        return abs(self.koeff[-1]) <= abs(other.koeff[-1])
    def __ge__(self,other):
        return other.__le__(self)
           
    


    

'''Tests'''
p1 = Polynom([-6, 1, 1])
print(p1.zeros())              # (2.0, -3.0)

p2 = Polynom([1, 0, 1])
print(p2.zeros())              # None

p3 = Polynom([1, 2, 3, 4])
try:                           # ← try/except damit kein Absturz
    print(p3.zeros())
except ValueError as e:
    print(e)

p4 = p1 + p3
print(p4.koeff)                # [-5, 3, 4, 4]

p = Polynom([1, 2, 3])
print((p * 4).koeff)      # [4, 8, 12]
print((4 * p).koeff)      # [4, 8, 12]
print((p * 0).koeff)      # [0]

p1 = Polynom([1, 2])
p2 = Polynom([3, 1])
print((p1 * p2).koeff)    # [3, 7, 2]

p1 = Polynom([1, 0, 3])
print(p1)              # 1 + 3x^2

p2 = Polynom([0, 2, 0, 4])
print(p2)              # 2x + 4x^3

p3 = Polynom([0])
print(p3)              # 0

p1 = Polynom([1, 2, 3])     # Grad 2
p2 = Polynom([5, 0])        # Grad 1
p3 = Polynom([4, 0, 1])     # Grad 2, höchster Koeff = 1

print(p1 <= p2)    # False  (Grad 2 > Grad 1)
print(p1 >= p2)    # True
print(p1 <= p3)    # False  (|3| > |1|)
print(p3 <= p1)    # True