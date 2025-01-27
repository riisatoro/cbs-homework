# Завдання 7

# Створіть ієрархію класів транспортних засобів. 
# У загальному класі опишіть загальні всім транспортних засобів поля,
# у спадкоємцях – специфічні їм. 
# Створіть кілька екземплярів. Виведіть інформацію щодо кожного транспортного засобу.


class BaseVehicle:
    def __init__(self, model: str, vin: str, max_speed: int, color: str,
                engine_type: str, manufacturer: str, door_amount: int, has_autopilot: bool = False
    ):
        self.model = model
        self.vin = vin
        self.max_speed = max_speed
        self.color = color
        self.engine_type = engine_type
        self.manufacturer = manufacturer
        self.door_amount = door_amount
        self.has_autopilot = has_autopilot
    
    def __str__(self):
        return (
            f"<{self.model} ({self.vin}), {self.color}. "
            f"Max speed is {self.max_speed} thanks to the {self.engine_type} engine. "
            f"With {self.door_amount} door(s) made by {self.manufacturer} you can" + (" " if self.has_autopilot else "'t ") + "even use autopilot\n"
        )


class Truck(BaseVehicle):
    def __init__(self, cargo_type: str, max_weight: float, oversized_cargo: bool = False, *args):
        super().__init__(*args)
        self.cargo_type = cargo_type
        self.max_weight = max_weight
        self.oversized_cargo = oversized_cargo
    
    def __str__(self):
        base_info = super().__str__()
        return (
            base_info + f"You can deliver up to {self.max_weight} tons of {self.cargo_type}. "
            "This vehicle can" + (" " if self.oversized_cargo else "'t ") + "deliver oversided cargo\n"
        )


class Submarine(BaseVehicle):
    def __init__(self, max_dive_depth: float, underwater_duration: int, *args):
        super().__init__(*args)
        self.max_dive_depth = max_dive_depth
        self.underwater_duration = underwater_duration
    
    def __str__(self):
        base_info = super().__str__()
        return base_info + f"You can dive up to {self.max_dive_depth} meters for {self.underwater_duration} minutes"

car = BaseVehicle("Mazda 2000", "2345-5456-4524", "220", "red", "v4 diesel", "Mazda Inc.", 4, True)
truck = Truck("medicine", 0.5, False, "Scania Power v2", "777-234", "120", "white", "v6 diesel-electric", "Scania LLC.", 2, True)
submarine = Submarine(125.8, 120, "Personal Submarine", "N/A", "60", "black granite", "v24 diesel", "Toyota", 1, False)

print(car)
print(truck)
print(submarine)
