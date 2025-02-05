class ReversedIter:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        self.index = len(self.value) - 1
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
    
        value = self.value[self.index]
        self.index -= 1
        return value



for i in ReversedIter([1, 2, 3, 4, 5]):
    print(i, end=" ")
print()