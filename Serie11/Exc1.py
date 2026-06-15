import numpy as np
import matplotlib.pylab as plt
import math



class MyFunction:
    def __init__(self, func, a, b): 
        self.func = func 
        self.a = a 
        self.b = b

    def __call__(self, x):
        if self.a <= x <= self.b:
            return self.func(x)
        else:
            raise ValueError(f'{x} nicht in [{self.a}, {self.b}]')

    def plot(self, x1=None, x2=None):
        if x1 is None:
            x1 = self.a #kein x angegeben --> nimmt die untere/obere Grenze
        if x2 is None:
            x2 = self.b
        
        x_vals = np.linspace(x1, x2, 100)
        y_vals = [self(x) for x in x_vals]

        plt.plot(x_vals, y_vals)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('MyFunction')
        plt.show()

f = MyFunction(math.sin, 0, 2 * math.pi)
print(f(1))
f.plot()
f.a = -5
f.plot()

g = MyFunction(lambda x: x**3 -x, -2, 2)
g.plot(-1, 1)

'''Test'''
f = MyFunction(lambda x: x**2, 0, 10)
print(f(3))    # 9
try:
    f(15)
except ValueError as e:
    print(e)   # ValueError
f.plot()


