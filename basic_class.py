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

my_Toyota = Car("red", "Toyota", "Corolla")
my_Toyota.start()
my_Toyota.stop()

my_Civic = Car("blue", "Honda", "Civic")
my_Civic.start()
my_Civic.accelerate(30)
my_Civic.stop()
