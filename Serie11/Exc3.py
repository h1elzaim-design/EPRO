import numpy as np
import matplotlib.pyplot as plt

def newton_plot(f, fprime, x0, x1, tol=1e-10, max_iter=100):
    xk = x0
    for k in range(max_iter):
        fxk = f(xk) # wert der funktion
        dfxk = fprime(xk) #steigung der tang
        
        if abs(fxk) < tol:
            break
            
        x_new = xk - fxk / dfxk
        
        # Plot vorbereiten
        span = 1.5 * abs(x0 - x1) #breite 1.5 mal der abstan zwischen x0 und x1
        x_left = xk - span
        x_right = xk + span # linke und rechte grenze
        x_vals = np.linspace(x_left, x_right, 200)
        
        plt.figure()
        plt.plot(x_vals, [f(x) for x in x_vals], 'b-', label='f(x)') #blaue kurve f(x)
        plt.axhline(0, color='black', lw=0.8)   # x achse schwarz
        plt.scatter([xk], [fxk], color='blue', s=80, zorder=5, label=f'Punkt x_{k}') #markiert akt. Punkt
        
        tangent = [fxk + dfxk * (x - xk) for x in x_vals] #tangente
        plt.plot(x_vals, tangent, 'g--', label='Tangente')
        plt.scatter([x_new], [0], color='red', s=80, zorder=5, label=f'x_{k+1}') # schnittpunkt mit x achse
        
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Newton Schritt {k+1}')
        plt.legend()
        plt.show()
        
        xk = x_new #nächster punkt: wiederhole

# Test:
f = lambda x: x**3 - x - 2
fprime = lambda x: 3*x**2 - 1
newton_plot(f, fprime, 2, 1)