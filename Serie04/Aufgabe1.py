code = input("code = ")
n = len(code)

is_a = (n % 2 == 0) and (code [0::2] == code [1::2])
is_b = (n % 2 == 0) and (code [:n//2] == code [n//2:])

result = (
    f"{code[0::2]} or {code[:n//2]}" if is_a is True and is_b is True else
    f"{code[0::2]}" if is_a is True else
    f"{code[:n//2]}" if is_b is True else
    "Keine Verdoppelung"
)

print(result)