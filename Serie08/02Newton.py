import math


def diff(f, x, h0, eps):
    h = h0
    phi_curr = (f(x + h) - f(x)) / h

    while True:
        h = h / 2
        phi_next = (f(x + h) - f(x)) / h

        if abs(phi_next - phi_curr) <= eps * abs(phi_curr):
            return phi_next

        phi_curr = phi_next


def newton(f, fprime, x0, tol=1e-8):
    x = x0

    while True:
        fx = f(x)
        fpx = fprime(x)

        if abs(fpx) <= tol * abs(fx):
            print("Warnung: Ableitung zu klein!")
            return None

        x_new = x - fx / fpx

        if abs(fx) < tol or abs(x_new - x) < tol:
            return x_new

        x = x_new


def newton_auto(f, x0, tol=1e-8, h0=1e-5, eps=1e-10):
    x = x0

    while True:
        fx = f(x)
        fpx = diff(f, x, h0, eps)

        if abs(fpx) <= tol * abs(fx):
            print("Warnung: Ableitung zu klein!")
            return None

        x_new = x - fx / fpx

        if abs(fx) < tol or abs(x_new - x) < tol:
            return x_new

        x = x_new


print("=== TESTS diff ===")
print(diff(lambda x: x**2, 2.0, 1.0, 1e-6))
print(diff(lambda x: x**3, 2.0, 1.0, 1e-6))

print("=== TESTS newton ===")
print(newton(lambda x: x**2 - 2, lambda x: 2*x, 1.0))

print("=== TESTS newton_auto ===")
print(newton_auto(lambda x: x**2 - 2, 1.0))

print("=== TESTS mit Prüfung ===")
print(math.isclose(diff(lambda x: x**2, 2.0, 1.0, 1e-6), 4.0, rel_tol=1e-5))
print(math.isclose(newton(lambda x: x**2 - 2, lambda x: 2*x, 1.0), math.sqrt(2), rel_tol=1e-8))
print(math.isclose(newton_auto(lambda x: x**2 - 2, 1.0), math.sqrt(2), rel_tol=1e-8))