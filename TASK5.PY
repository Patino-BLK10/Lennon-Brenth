class Employee:
    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def give_raise(self, amount):
        self.salary += amount  
    
    def display_employee(self):
        print(f"Employee Name  : {self.name}")
        print(f"Job Position   : {self.position}")
        print(f"Monthly Salary : {self.salary}")


bren = Employee( "Brenth Patino", "Senior Developer", 20000)


bren.display_employee()

bren.give_raise(10000)

print("\nAfter Raise:")
bren.display_employee()
