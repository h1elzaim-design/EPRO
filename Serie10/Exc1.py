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




'''Test'''
p = Polynom([1, 2, 3])
p2 = p.deriv()
print(p2.koeff)
print(p2.eval(1))
print(p.koeff)
print(p.grad)
print(p.eval(0))
print(p.eval(2))
print(p.eval(1))
'''Test'''
p1 = Polynom([-6, 1, 1])
print(p1.zeros())              # (2.0, -3.0)

p2 = Polynom([1, 0, 1])
print(p2.zeros())              # None

p3 = Polynom([1, 2, 3, 4])
try:
    print(p3.zeros())
except ValueError as e:
    print(e)                   # "Nur für Polynome 2.Grades"