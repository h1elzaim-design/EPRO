import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**3 - x - 2
fprime = lambda x: 3*x**2 - 1

# Bisektion - sammelt alle Zwischenschritte
def bisection_steps(f, a, b, tol=1e-10):
    steps = []
    while b - a > 2 * tol: # solange intrvall zu gross: weiter
        m = (a + b) / 2 #bisektion, MP d Interv.
        steps.append(m)
        if f(a) * f(m) <= 0: #vorzeichen check
            b = m
        else:
            a = m
    return steps

# Newton - sammelt alle Zwischenschritte
def newton_steps(f, fprime, x0, tol=1e-10, max_iter=100):
    steps = []
    x = x0
    for _ in range(max_iter):
        steps.append(x)
        if abs(f(x)) < tol:
            break
        x = x - f(x) / fprime(x)
    return steps

# Schritte berechnen
steps_bi = bisection_steps(f, 1, 3)
steps_nw = newton_steps(f, fprime, 2)

# Fehler berechnen
errors_bi = [abs(f(x)) for x in steps_bi] #wie weit noch entfernt
errors_nw = [abs(f(x)) for x in steps_nw]

# Plot normal
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(errors_bi, 'o-', label='Bisektion')
ax1.plot(errors_nw, 's-', label='Newton')
ax1.set_xlabel('Iteration i')
ax1.set_ylabel('|f(x_i)|')
ax1.set_title('Konvergenz (normal)')
ax1.legend()

# Plot logarithmisch
ax2.semilogy(errors_bi, 'o-', label='Bisektion')
ax2.semilogy(errors_nw, 's-', label='Newton')
ax2.set_xlabel('Iteration i')
ax2.set_ylabel('|f(x_i)|')
ax2.set_title('Konvergenz (logarithmisch)')
ax2.legend()

plt.tight_layout()
plt.show()