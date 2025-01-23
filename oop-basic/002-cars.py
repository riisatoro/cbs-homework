# Завдання 4
#
# Створіть клас, який описує автомобіль. 
# Створіть клас автосалону, що містить в собі список автомобілів, 
# доступних для продажу, і функцію продажу заданого автомобіля.


class Car:
    def __init__(self, model: str, power: int, color: str, price: float):
        self.model = model
        self.power = power
        self.color = color
        self.price = price
    
    def print_info(self):
        print(f"{self.model} {self.power} HP, {self.color}, ${self.price}")
    
    def __str__(self):
        return f"<{self.model} {self.price}>"

    def __eq__(self, value: "Car"):
        return self.model == value.model
    
    def __eq__(self, value: str):
        return self.model == value


class Dealer:
    def __init__(self, name: str, cars: list[Car] | None = None):
        self.name = name
        self.cars = cars or list()
        self.profit = 0
    
    def add_car(self, car: Car):
        self.cars.append(car)
    
    def sell_car(self, car: Car | str):
        try:
            sell_car_index = self.cars.index(car)
            self.profit += self.cars[sell_car_index].price
            selled_car = self.cars.pop(sell_car_index)
            print(car, f"was sold. +{selled_car.price}$")
        except ValueError:
            print("Car {} does not exists.")

    def print_info(self):
        print(f"{self.name}, {len(self.cars)} cars, profit: ${self.profit}")


cars = [
    Car("Mazda", 220, "white", 38000),
    Car("Opel", 180, "red", 29000),
    Car("Toyota", 720, "black", 42000),
]

dealer = Dealer("TopCarSeller", cars=cars)

dealer.print_info()
dealer.sell_car("Mazda")
dealer.add_car(Car("Mazda 2025", 360, "grey", 78000))
dealer.sell_car("Mazda 2025")
dealer.print_info()
dealer.sell_car("Nonexisted")
