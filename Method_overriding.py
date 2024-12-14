class Car:
    def __init__(self, color, brand, model, speed=0):
        self.color = color
        self.brand = brand
        self.model = model
        self.speed = speed

    def start(self):
        print(f"The {self.color} {self.brand} {self.model} is starting.")

    def stop(self):
        print(f"The {self.color} {self.brand} {self.model} is stopping.")

    def accelerate(self, increment):
        self.speed += increment
        print(f"The {self.color} {self.brand} {self.model} is now going.")

class  Motorcycle(Car):
    def display_info(self):
        print(f"Motorcycle: {self.brand} {self.model} {self.color}")

moto = Motorcycle("Honda", "CBR500", 2021)
moto.display_info()