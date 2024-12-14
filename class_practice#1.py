class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self._age = age
        self.gender = gender

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            raise ValueError("Age must be greater than zero")
        
    def display_info(self):
        print(f"My Name is {self.name} I am {self.age} Year olds and My gender is {self.gender} Nice to meet You.")


person = Person("Michael", 30, "Male")
person.display_info()
# person.age = 0 An error will occur
#test add to git