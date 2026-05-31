class Polynom:
    def __init__(self, koeff):
        self.koeff = koeff
        self.grad = len(koeff) - 1

    def __add__(self, other):
        n = max(len(self.koeff), len(other.koeff))
        a = self.koeff + [0] * (n - len(self.koeff))
        b = other.koeff + [0] * (n - len(other.koeff))
        return Polynom([a[i] + b[i] for i in range(n)])

    def __mul__(self, other):
            if isinstance(other, (int, float)):
                if other == 0:
                    return Polynom([0])
                return Polynom([a * other for a in self.koeff])
            elif isinstance(other, Polynom):
                c = [0] * (self.grad + other.grad + 1)
                for i in range(self.grad + 1):
                    for j in range(other.grad + 1):
                        c[i+j] += self.koeff[i] * other.koeff[j]
                return Polynom(c)

    def __rmul__(self, other):
        return self.__mul__(other)

'''Test'''
p1 = Polynom([1, 2])
p2 = Polynom([3, 0, 5])
p3 = p1 + p2
print(p3.koeff)    # [4, 2, 5]
p = Polynom([1, 2, 3])
print((p * 4).koeff)     # [4, 8, 12]
print((4 * p).koeff)     # [4, 8, 12]
print((p * 0).koeff)     # [0]