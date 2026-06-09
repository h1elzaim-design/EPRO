class Counter:
    def __init__(self, start):
        self.start = start
    def __call__(self):
        self.start += 1
        return self.start