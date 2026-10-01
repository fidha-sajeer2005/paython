class Car:
    def __init__(self,make,model,year,price):
        self.make=make
        self.model=model
        self.year=year
        self.price=price

    def display_info(self):
        print(f"Car:{self.year} {self.make} {self.model}price is {self.price}")

car1=Car("honda", "civic", 2022, 5000000)
car1.display_info()
car2=Car("ford","mustag", 2001, 7000000)
car2.display_info()
print(car1)


class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.__salary = salary

    def display_employee(self):
        print(f"name: {self.name},  {self.__salary}")

    def add_money(self, new_amount):
        self.__salary += new_amount

emp = Employee("john", 50000)
emp.display_employee()

emp.add_money(5000)
emp.display_employee()

print(emp.name)
