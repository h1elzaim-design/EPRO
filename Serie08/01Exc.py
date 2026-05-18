def diff(f, x, h0, eps):
    h = h0
    phi_curr = (f(x + h) - f(x)) / h

    while True:
        h = h / 2
        phi_next = (f(x + h) - f(x)) / h

        if abs(phi_next - phi_curr) <= eps * abs(phi_curr):
            return phi_next

        phi_curr = phi_next


print(diff(lambda x: x**2, 3.0, 1.0, 1e-6))
print(diff(lambda x: x**3, 2.0, 1.0, 1e-6))
print(diff(lambda x: x**2, 2.0, 0.5, 1e-6))
print(diff(lambda x: x**3, 2.0, 0.5, 1e-6))

