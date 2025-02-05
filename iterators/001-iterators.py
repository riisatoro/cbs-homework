# Завдання 1
# 
#  Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable


class CustomIterable:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.value):
            raise StopIteration
    
        value = self.value[self.index]
        self.index += 1
        return value


for i in CustomIterable("ababagalamaga"):
    print(i, end=" ")

print()

for i in CustomIterable([1, 2, 3, 4, 5]):
    print(i, end=" ")

print()
