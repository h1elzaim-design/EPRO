class TimeInterval:
    def __init__(self, start, end):
        if end < start:
            print('Fehler: end muss größer als start sein')
            return
        self.start = start
        self.end = end

    def __str__(self):
        return f'[{self.start}, {self.end}]'

    def __repr__(self):
        return f'[{self.start}, {self.end}]'

    def __lt__(self, other):
        return self.start < other.start



'''Test'''
t1 = TimeInterval(1, 5)
t2 = TimeInterval(2, 3)
t3 = TimeInterval(0, 4)
t4 = TimeInterval(5, 1)    # Fehler!

print(t1)                  # [1, 5]

lst = [t1, t2, t3]
print(sorted(lst))         # [[0, 4], [1, 5], [2, 3]]

print(t1<t2)
print(t2<t1)