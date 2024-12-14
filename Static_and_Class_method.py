class Vehicle:
    wheels = 4
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @staticmethod
    def vehicle_types():
        return ["Car", "Truck", "Motorcycle"]

    @classmethod
    def default_vehicle(cls):
        return cls("Default Brand", "Default Model", 2020)

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")


print(Vehicle.vehicle_types())

default_vehicle = Vehicle.default_vehicle()
default_vehicle.display_info()
