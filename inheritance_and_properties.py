class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self._year = year 

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        if value >= 1886:
            self._year = value
        else:
            raise ValueError("Year must be 1886 or later")

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

    
class Car(Vehicle):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year)
        self.color = color

    def display_car_info(self):
        print(f"This is a {self.color} {self.year} {self.brand} {self.model}")

mycar = Car("Toyota", "Camry", 2020, "red")
mycar.display_info()
mycar.display_car_info()

mycar2 = Vehicle("Ford", "Mustang", 1965)
print(mycar2.year)
mycar2.year = 2022
print(mycar2.year)
mycar2.year = 1800 # An error will occur
