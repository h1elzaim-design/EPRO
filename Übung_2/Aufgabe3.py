pi = 3.14159
x = eval(input("Zahl x: "))
fehler = abs(pi-x)/pi
prozent = fehler * 100
print(f"Pi kann durch {x} approximiert werden mit einem relativen Fehler von {prozent:.2f}%.")