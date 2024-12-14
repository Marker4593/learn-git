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
        print(
            f"My Name is {self.name} I am {self.age} Year olds and My gender is {self.gender} Nice to meet You."
        )


class Employee(Person):
    def __init__(self, name, age, gender, position, salary):
        super().__init__(name, age, gender)
        self.position = position
        self.salary = salary

    @staticmethod
    def company_policies():
        print("All employees must adhere to company policies.")
    
    @classmethod
    def default_employee(cls):
        return cls("Default Name", 30, "Not Specified", "Staff", "30,000")

    def display_full_info(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Position: {self.position}, Salary: {self.salary}"
        )

Employee.company_policies()
defalut_employee = Employee.default_employee()
defalut_employee.display_full_info()
